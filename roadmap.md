# Roadmap: Future Development

This roadmap outlines the planned improvements and research directions for the **Think then Translate (TPO)** project.

## 🟢 Phase 1: Refining the Reasoning Model (Short Term)
- [ ] **Extended DPO Iterations**: Run 3-5 more iterations of DPO to bridge the performance gap between TPO and non-reasoning models.
- [ ] **Reasoning Length Optimization**: Experiment with forcing longer reasoning steps for "Hard" difficulty examples to capture deep philosophical nuances.
- [ ] **Error Analysis & Mitigation**: Conduct a post-mortem on cases where the model repeats itself or hallucinations occur in the reasoning block.

## 🔵 Phase 2: Online & Real-time Optimization (Medium Term)
- [ ] **Online DPO**: Implement real-time preference learning using Claude 3.5 Sonnet as an online reward model.
- [ ] **Dedicated Reward Model**: Train a specialized BERT-based or Llama-based reward model tailored specifically for Tibetan Buddhist translation quality.
- [ ] **Technical Term Enforcement**: Integrate a "technical dictionary" constraint into the reward model to penalize incorrect usage of established terminology.

## 🔴 Phase 3: Reasoning Agents & RLHF (Long Term)
- [ ] **Agentic Translation**: Develop an agent that can pause during the "thinking" phase to:
    - Search external Buddhist dictionaries (e.g., 84000, Christian Wedemeyer's dictionary).
    - Retrieve similar translation examples from a vector database.
    - Consult canonical commentaries.
- [ ] **Human-in-the-loop RLHF**: Collect feedback from expert human translators to create a high-fidelity preference dataset.
- [ ] **Multimodal Reasoning**: Incorporate image-to-reasoning capabilities for translating from digitized woodblock prints or manuscripts.

## 🎯 Goal
To create the world's most accurate and interpretable translation system for Tibetan literature, capable of providing scholars and practitioners with not just a translation, but a reasoned explanation of the linguistic and philosophical choices behind it.


