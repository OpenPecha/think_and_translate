# Data Pipeline

## Overview

```
84k pairs → Extract 33k self-contained units → Generate thoughts → Training data
```

## Step 1: Extraction

**Source**: 84,000 Tibetan-English pairs from Buddhist literature.

**Output**: 33,000 self-contained units.

**Rules**:
- Each unit must be complete (no orphaned sentences)
- 1:1 alignment or combined adjacent rows
- No repetitive Buddhist phrases

**Code**: `main.py`

## Step 2: Thought Generation

**Model**: Claude 3.5 Sonnet

**Prompt** (from `Prompts.md`):
```
Generate the internal thought process of an expert Buddhist translator...
Thoughts should lead to the exact translation word for word!
```

**Output Format**:
```
<t>
[Reasoning about terms, structure, meaning]
</t>
[Final Translation]
```

**Code**: `claude_inference_simple_template.py`

## Sample Data

**Source (Tibetan)**:
```
བཀའ་སྩལ་པ། བྱམས་པ་ངས་ཆོས་གདགས་པ...
```

**Thought**:
```
<t>
First, "བཀའ་སྩལ་པ།" is a formal speech marker...
"བྱམས་པ" is Maitreya...
Now we have a list of Buddhist text types...
</t>
```

**Translation**:
```
Maitreya, I have set forth the Dharma in the following way...
```

