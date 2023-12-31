# import openai
import os

from agents.BaseAgent import BaseAgent
# # import openai

class LLMAgent(BaseAgent):
    def __init__(self, api_key=None, **kwargs):
        super().__init__(name="LLMAgent")
        self.api_key = api_key if api_key else os.getenv('OPENAI_API_KEY')

    def play_move(self, prompt: str) -> str:
        # openai.api_key = self.api_key
        try:
            
            response = type('', (), {})()
            response.choices = [type('', (), {})()]
            response.choices[0].text = 'rock'

            move = response.choices[0].text.strip()
            return move
        except Exception as e:
            print(f"Error interfacing with OpenAI API: {e}")
            # Fallback to a random move in case of an error
            import random
            return random.choice(["R", "P", "S"])

    def update_api_key(self, new_api_key: str):
        """Update the API key for the LLMAgent."""
        self.api_key = new_api_key
