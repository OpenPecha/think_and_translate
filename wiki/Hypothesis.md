# Hypothesis

## Core Belief

> Incorporating explicit chain-of-thought (CoT) reasoning into the translation process significantly enhances translation quality compared to direct translation.

## Why It Works

1. **Mirrors Human Process**: Expert translators analyze, reason, then translate—not in one step.
2. **Handles Complexity**: Buddhist texts contain technical terms, philosophical nuances, and cultural context.
3. **Interpretability**: Users can see *why* a translation was chosen.

## The OpenAI o1 Demonstration

Hyung Won (OpenAI) showed a corrupted Korean sentence with unnecessary consonants:
- **GPT-4**: Failed to translate correctly
- **O1**: Deciphered → Reasoned → Translated accurately

This structured approach is what TPO brings to Tibetan-English translation.

## What We Test

| Model | Approach |
|-------|----------|
| Direct | Source → Translation |
| TPO | Source → `<t>Reasoning</t>` → Translation |

We measure if TPO produces better translations using BLEURT, BLEU, and human evaluation.

