from trl import BasePairwiseJudge
import torch
from bleurt_pytorch import BleurtConfig, BleurtForSequenceClassification, BleurtTokenizer

class BleuRTJudge(BasePairwiseJudge):
    def __init__(self, model_name='lucadiliello/BLEURT-20', device='cuda:0'):
        """
        Initialize the BLEURT model and tokenizer.
        """
        self.device = device
        self.model = BleurtForSequenceClassification.from_pretrained(model_name).to(self.device)
        self.tokenizer =BleurtTokenizer.from_pretrained(model_name)

    def bleurt_score(self, prompt, completions):
        """
        Compute BLEURT scores for a single prompt with two completions.
        """
        with torch.no_grad():
            # Tokenize the prompt with each completion
            inputs = self.tokenizer(
                [prompt] * len(completions),  # Duplicate the prompt for each completion
                completions, 
                padding='longest', 
                return_tensors='pt'
            )
            inputs = inputs.to(self.device)  # Send inputs to the correct device
            scores = self.model(**inputs).logits.flatten().tolist()  # Get BLEURT scores
        return scores

    def judge(self, prompts, completions, shuffle_order=False):
        """
        Compare completions for each prompt and determine the preferred completion.
        """
        preferences = []
        for prompt, completion_pair in zip(prompts, completions):
            scores = self.bleurt_score(prompt, completion_pair)
            preferences.append(0 if scores[0] > scores[1] else 1)
        return preferences