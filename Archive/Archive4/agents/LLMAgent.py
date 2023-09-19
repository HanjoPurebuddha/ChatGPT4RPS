
from agents.BaseAgent import BaseAgent
import openai

class LLMAgent(BaseAgent):
    def __init__(self, api_key: str):
        super().__init__(name="LLMAgent")
        self.api_key = api_key

    def play_move(self, prompt: str) -> str:
        openai.api_key = self.api_key
        try:
            response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=10)
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
