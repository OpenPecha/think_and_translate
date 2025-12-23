# Data Pipeline Documentation

This document describes the process of preparing the dataset for the **Think then Translate (TPO)** model.

## 1. Source Dataset
- **Volume**: ~84,000 Tibetan-English text pairs.
- **Nature**: High-quality parallel corpora, primarily Buddhist literature.

## 2. Extraction & Curation
Using `main.py`, we processed the raw dataset to extract **33,000 self-contained units**. 

### Extraction Rules:
- **Self-Containment**: Each unit must carry complete meaning in isolation (no orphaned sentences).
- **Alignment**: Direct 1:1 matches or intelligently combined adjacent rows forming logical paragraphs.
- **Deduplication**: Avoided common repetitive phrases in Buddhist literature.
- **Quality**: No truncated content or misaligned translations.

## 3. Synthetic Thought Generation
The core of our approach is the generation of synthetic "thoughts" (rationales) that lead to the ground-truth translation. This was implemented in `claude_inference_simple_template.py`.

### The Thought Generation Prompt:
The model (Claude 3.5 Sonnet) is prompted to act as an **expert Buddhist translator**.
- **Input**: Source (Tibetan) + Ground Truth (English).
- **Task**: Generate an internal thought process (enclosed in `<t>...</t>`) that logically leads to the *exact* ground-truth translation.
- **Nuance**: Complexity of thoughts scales with text difficulty.

### Prompt Logic:
```markdown
Generate the internal thought process of an expert Buddhist translator...
The thoughts should reflect the translator’s reasoning, linguistic considerations, and cultural reflections...
Thoughts should lead to the exact translation word for word!
```

## 4. Dataset Post-Processing
- **Difficulty Classification**: Claude was used to classify examples into *Hard*, *Medium*, and *Low* difficulty.
- **Formatting**: The final training data follows the structure:
  ```
  [Source Tibetan] -> <t> [Generated Reasoning] </t> [Final Translation]
  ```

## 5. Pairwise Preference Data
For the DPO phase, we utilized `Judges.py` to compare candidate translations (generated with temperature sampling) against the ground truth using BLEURT. This created the "Chosen" vs "Rejected" pairs required for DPO.


