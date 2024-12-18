import time
import json
import logging
from pathlib import Path
from datasets import load_dataset
from tqdm.notebook import tqdm
from anthropic import Anthropic, BadRequestError
from datasets import Dataset

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


ANTHROPIC_API_KEY = "API"
client = Anthropic(api_key=ANTHROPIC_API_KEY)
RPM = 4000  # Requests per minute
INPUT_TOKENS_PER_MINUTE = 400000
OUTPUT_TOKENS_PER_MINUTE = 80000
from concurrent.futures import ThreadPoolExecutor, as_completed
CHUNK_SIZE = 200

def count_tokens(text):

    return client.count_tokens(text)

MODEL_NAME = "claude-3-5-sonnet-20240620"
RPM = 4000  
INPUT_TOKENS_PER_MINUTE = 400000
OUTPUT_TOKENS_PER_MINUTE = 80000

def build_prompt(tsv_text: str) -> str:
    prompt = f"""
**TSV:**
{tsv_text}

**Prompt:**


Analyze this TSV file containing Tibetan-English text pairs and extract well-aligned content pairs, following these rules:

1. ALIGNMENT STRATEGIES:
   - Look for direct 1:1 matches between Tibetan and English columns
   - Intelligently combine adjacent rows when they form part of the same logical paragraph
   - Consider contextual clues like punctuation and sentence completeness
   
2. EXTRACTION CRITERIA:
   - Each pair must form a complete, self-contained unit of meaning
   - Both Tibetan and English sides must be coherent and logically complete
   - Can be either a full paragraph or a well-formed single sentence
   - Must maintain accurate translation alignment
   - Donot extract lines and text that repeats in buddhist letrature in general 

3. COMBINATION RULES:
   - When combining rows, ensure semantic continuity
   - Look for incomplete sentences that complete in adjacent rows
   - Check for paragraph breaks and topic shifts
   - Maintain parallel structure between Tibetan and English sides

4. OUTPUT FORMAT:
   ```
   <p>
   Tibetan: [combined/single Tibetan text]
   English: [combined/single English text]
   </p>
   ```

5. QUALITY REQUIREMENTS:
   - No truncated or incomplete content
   - No misaligned translations
   - No orphaned sentences requiring external context
   - Preserve exact text as it appears in source


**Output all valid pairs in the specified format, ensuring complete coverage of the file.**

Please make sure you have maximun of best 20 pairs or less, not more then that, so start with the best combined text or sentence 


"""
    return prompt.strip()

def call_api(prompt: str, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model=MODEL_NAME,
                max_tokens=8192,
                temperature=0,
                messages=[{"role": "user", "content": prompt}]
            )
            return response
        except BadRequestError as e:
            err_str = str(e)
            if "prompt is too long" in err_str:
                raise e
            else:
                logging.error(f"BadRequestError: {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
        except Exception as e:
            logging.error(f"API call failed on attempt {attempt+1}: {e}")
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)

def process_chunk(
    tsv_text: str, 
    file_name: str, 
    global_index: int, 
    requests_made: int, 
    start_time: float, 
    tokens_used_input: int, 
    tokens_used_output: int, 
    f_out
):
    """
    Attempt to process the given TSV chunk. If too long, recursively halve it until it fits.
    """

    elapsed = time.time() - start_time
    if requests_made >= RPM:
        sleep_time = 60 - elapsed
        if sleep_time > 0:
            logging.info(f"Sleeping {sleep_time} seconds to comply with RPM.")
            time.sleep(sleep_time)
        requests_made = 0
        start_time = time.time()
        tokens_used_input = 0
        tokens_used_output = 0

    prompt = build_prompt(tsv_text)

    try:
        response = call_api(prompt)
        response_text = response.content[0].text
        usage = response.usage

        # Update usage counters
        requests_made += 1
        tokens_used_input += usage.input_tokens
        tokens_used_output += usage.output_tokens

        # Save result
        result = {
            "input_file":tsv_text,
            "global_index": global_index,
            "file_name": file_name,
            "response": response_text,
            "usage": {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens
            }
        }
        f_out.write(json.dumps(result, ensure_ascii=False) + "\n")

        return requests_made, start_time, tokens_used_input, tokens_used_output, global_index + 1

    except BadRequestError:
        # Prompt too long, halve it
        logging.info("Prompt too long, splitting into halves...")
        lines = tsv_text.split("\n")
        if len(lines) <= 1:
            # Even a single line failed, skip it
            logging.warning("Single line prompt too large. Skipping this line.")
            return requests_made, start_time, tokens_used_input, tokens_used_output, global_index

        mid = len(lines) // 2
        first_half = "\n".join(lines[:mid])
        second_half = "\n".join(lines[mid:])

        # Process first half
        requests_made, start_time, tokens_used_input, tokens_used_output, global_index = process_chunk(
            first_half, file_name, global_index,
            requests_made, start_time, tokens_used_input, tokens_used_output, f_out
        )

        # Process second half
        requests_made, start_time, tokens_used_input, tokens_used_output, global_index = process_chunk(
            second_half, file_name, global_index,
            requests_made, start_time, tokens_used_input, tokens_used_output, f_out
        )

        return requests_made, start_time, tokens_used_input, tokens_used_output, global_index

def process_file_text(tsv_text, file_name, global_index, requests_made, start_time, tokens_used_input, tokens_used_output, f_out):
    lines = tsv_text.split("\n")
    for start in range(0, len(lines), CHUNK_SIZE):  # Removed tqdm here
        chunk_lines = lines[start:start+CHUNK_SIZE]
        chunk_text = "\n".join(chunk_lines)
        requests_made, start_time, tokens_used_input, tokens_used_output, global_index = process_chunk(
            chunk_text, file_name, global_index, requests_made, start_time, tokens_used_input, tokens_used_output, f_out
        )
    return requests_made, start_time, tokens_used_input, tokens_used_output, global_index

def process_batch(batch, global_index, requests_made, start_time, tokens_used_input, tokens_used_output, f_out):
    batch_results = []
    for row in batch:
        tsv_text = row["text"]
        file_name = row["file_name"]

        requests_made, start_time, tokens_used_input, tokens_used_output, global_index = process_file_text(
            tsv_text, file_name, global_index, requests_made, start_time, tokens_used_input, tokens_used_output, f_out
        )


        batch_results.append((requests_made, start_time, tokens_used_input, tokens_used_output, global_index))

    return batch_results
def main():
    output_path = Path("responses_final_3.jsonl")
    dataset= load_dataset("PATH")


    requests_made = 0
    start_time = time.time()
    tokens_used_input = 0
    tokens_used_output = 0
    global_index = 0

    batch_size = 5
    batches = [dataset[i:i+batch_size] for i in range(0, len(dataset), batch_size)]

    with ThreadPoolExecutor(max_workers=5) as executor, output_path.open("a", encoding="utf-8") as f_out:
        future_to_batch_index = {}
        
        for batch_index, batch in enumerate(batches):
            batch = Dataset.from_dict(batch)
            
            future = executor.submit(
                process_batch, batch, global_index, requests_made, start_time, tokens_used_input, tokens_used_output, f_out
            )
            future_to_batch_index[future] = batch_index


        for future in tqdm(as_completed(future_to_batch_index), total=len(batches), desc="Processing"):
            batch_results = future.result()

            requests_made, start_time, tokens_used_input, tokens_used_output, global_index = batch_results[-1]

    logging.info("Processing complete.")

if __name__ == "__main__":
    main()