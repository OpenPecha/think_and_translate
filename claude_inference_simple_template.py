import anthropic
import time
import jsonlines
from datasets import load_dataset
import Pool, Manager
from tqdm.notebook import tqdm

# Initialize the client
client = anthropic.Anthropic(
    api_key="api",
)

# Function for inference
def inference_pc(args):
    example, filename, file_lock = args  # Unpack the arguments
    time.sleep(5)  # Simulate API rate-limiting
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8192,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"""
Given the following correct Translation from tibetan to english:
tibetan: f{example['tibetan']}
english: f{example['english']}

Generate the internal thought process of an expert Buddhist translator as they translate the given Tibetan text into the provided English ground truth. The thoughts should reflect the translator’s reasoning, linguistic considerations, and cultural reflections, as if they are actively working on the translation. Structure the thoughts naturally, beginning with <t> and ending with </t>. The thoughts should logically lead to the final translation, showcasing the decision-making process step-by-step. The complexity of the thoughts should match the difficulty of the text — longer, more nuanced thoughts for complex passages, and shorter, more straightforward thoughts for simpler ones. Assume the provided English translation is accurate and follows the thoughts. Thoughts should lead to the exact translation word for word!
DONT ACT LIKE YOU CAN SEE THE TRANSLATION IN THOUGHTS AS YOU ARE TRANSLATING IT-DO ANALYSIS ONLY CAUSE YOU HAVE TO GENERATE THOUGHTS!!
"""
                        }
                    ]
                }
            ]
        )
        # Add thoughts to the example
        example['thoughts'] = message.content[0].text

        # Save result to file incrementally
        with file_lock:
            with jsonlines.open(filename, mode='a') as writer:
                writer.write(example)

    except Exception as e:
        print(f"Error processing example {example}: {e}")


# Multiprocessing setup
def process_dataset(train_data, filename):
    # Ensure the file is empty before starting
    with open(filename, 'w') as f:
        pass

    # Use a Manager to handle the file lock for writing
    manager = Manager()
    file_lock = manager.Lock()

    # Prepare arguments for multiprocessing
    args = [(example, filename, file_lock) for example in train_data]

    # Use Pool for multiprocessing
    with Pool(processes=10) as pool:
        # Wrap the dataset with tqdm for a progress bar
        list(tqdm(
            pool.imap_unordered(inference_pc, args),
            total=len(train_data),
            desc="Processing examples"
        ))



# Run the process
if __name__ == "__main__":
    output_filename = 'results.jsonl'
    data_file = 'huggingface dataset path'
    train = load_dataset(data_file)
    process_dataset(train, output_filename)
