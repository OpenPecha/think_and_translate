# Think Then Translate (TPO) Wiki

Welcome to the **Think Then Translate** wiki! This project enhances Monlam Melong with reasoning-driven translation.

## Quick Links

| Page | Description |
|------|-------------|
| [[Hypothesis]] | Why "thinking before translating" works |
| [[Data-Pipeline]] | Dataset extraction and thought generation |
| [[Training]] | SFT and DPO training process |
| [[Evaluation]] | Metrics, baselines, and results |
| [[Future-Work]] | Roadmap and next steps |

## Project Overview

**Goal**: Enable Monlam Melong to generate internal reasoning (`<t>...</t>`) before producing translations, improving accuracy for complex Buddhist texts.

**Inspiration**: OpenAI o1 "Thinking LLM" paradigm.

**Demo**: [HuggingFace Space](https://huggingface.co/spaces/openpecha/Translation_TPO_demo)

## Key Results

- TPO outperforms Claude Direct on BLEURT
- Provides interpretable reasoning for each translation
- Currently 2 DPO iterations; more iterations expected to improve performance

