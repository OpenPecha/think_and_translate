# Think then Translate (TPO) - PMA0015: Making Melong Think !!

"Incorporating explicit chain-of-thought (CoT) reasoning into the translation process significantly enhances translation quality compared to direct translation."

This project, identified as **PMA0015**, aims to enhance **Monlam Melong** (a prominent translation tool) by introducing the ability to "think" before translating. Inspired by the "Thinking LLM" paradigm (OpenAI o1), we enable the model to generate internal rationales before producing final translations to improve contextual accuracy and logical coherence.

## 🚀 The Vision

Traditional machine translation often fails on complex, domain-specific texts (like Buddhist literature) or corrupted inputs. Our approach for Monlam Melong mirrors the human translation process:
1.  **Analyze**: Decipher the source, handle corruptions, and identify technical terms.
2.  **Reason**: Step-by-step logic to resolve ambiguities.
3.  **Translate**: Produce the final output based on the reasoned rationale.

## 📊 Key Results

Our experiments show that TPO models provide unique advantages in interpretability and technical accuracy. While currently performing slightly below top-tier non-reasoning models after only two DPO iterations, the trajectory suggests that further refinement will lead to state-of-the-art performance for specialized domains.

*   **Primary Metric**: BLEURT (for semantic alignment).
*   **Secondary Metric**: BLEU (for technical term verification).

For a detailed breakdown of metrics, win rates, and analysis, see [RESULTS.md](RESULTS.md).

## 🛠 Project Structure

- `main.py`: Data extraction and processing pipeline.
- `claude_inference_simple_template.py`: Synthetic thought generation using Claude 3.5 Sonnet.
- `Judges.py`: BLEURT-based pairwise judging for preference alignment.
- `Prompts.md`: Comprehensive list of prompts used for data curation and CoT generation.
- `DOCUMENTATION_TICKET.md`: Structured ticket for documenting this experiment.

## 🧪 Methodology

1.  **Dataset Preparation**: Extracted 33k self-contained units from a high-quality 84k dataset.
2.  **Synthetic CoT**: Generated reasoning-driven rationales for each translation.
3.  **SFT**: Trained a base model to generate `<t> reasoning </t>` before the translation.
4.  **DPO Iterations**: Used BLEURT and Claude-based ELO rankings to perform Direct Preference Optimization.

## 🔗 Links

- **Wiki**: [Full Documentation](https://github.com/OpenPecha/think_and_translate/wiki) | [Local Wiki](wiki/)
- **Demo**: [HuggingFace Translation TPO Demo](https://huggingface.co/spaces/openpecha/Translation_TPO_demo)
- **Project Board**: [OpenPecha GitHub Project](https://github.com/orgs/OpenPecha/projects/107)
