# **Prompt for generating self contained pairs**

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

# Prompt for generating thoughts

Given the following correct translation from Tibetan to English:
tibetan: f{example['tibetan']}
english: f{example['english']}

Generate the internal thought process of an expert Buddhist translator as they translate the given Tibetan text into the provided English ground truth. The thoughts should reflect the translator’s reasoning, linguistic considerations, and cultural reflections, as if they are actively working on the translation. Structure the thoughts naturally, beginning with `<t>` and ending with `</t>`. The thoughts should logically lead to the final translation, showcasing the decision-making process step-by-step. The complexity of the thoughts should match the difficulty of the text — longer, more nuanced thoughts for complex passages, and shorter, more straightforward thoughts for simpler ones. Assume the provided English translation is accurate and follows the thoughts. Thoughts should lead to the exact translation word for word!

**Note:**
DONT ACT LIKE YOU CAN SEE THE TRANSLATION IN THOUGHTS AS YOU ARE TRANSLATING IT
DONOT JUST DO ANALYSIS ONLY
YOU HAVE TO GENERATE THOUGHTS!!
