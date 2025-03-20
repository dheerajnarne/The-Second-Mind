from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ReflectionAgent:
    def __init__(self, model_name="EleutherAI/pythia-2.8b"):
        """Initialize the reflection agent with Pythia 2.8B"""
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name)  # Load model on GPU

    def reflect(self, idea, web_data=None):
        """Check the coherence of the idea and provide feedback"""
        if web_data:
            # Incorporate web data into the prompt
            web_context = "\n".join([f"- {item['title']}: {item['summary']}" for item in web_data])
            prompt = f"""Evaluate the coherence of the following research idea based on recent studies:
            
            Idea: {idea}
            
            Consider the following recent studies:
            {web_context}
            
            Provide feedback on the coherence of the idea and suggest improvements."""
        else:
            prompt = f"""Evaluate the coherence of the following research idea:
            
            Idea: {idea}
            
            Provide feedback on the coherence of the idea and suggest improvements."""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")  # Move inputs to GPU
        outputs = self.model.generate(**inputs, max_new_tokens=200)
        reflection = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return reflection