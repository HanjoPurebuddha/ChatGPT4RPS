
import openai

class LLMAgent(BaseAgent):
    def __init__(self, model="gpt-4-0613", max_tokens=7, temperature=0.5):
        super().__init__(name="LLMAgent")
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def play_move(self, opponent_move):
        if opponent_move in ["R", "P", "S"]:
            self.update_history(opponent_move)

        rps_sequence = " ".join(self.history)
        
        response = openai.Completion.create(
            model=self.model,
            prompt=f"RPS sequence: {rps_sequence}. What's the next move?",
            max_tokens=self.max_tokens,
            temperature=self.temperature
        )

        next_move = response.choices[0].text.strip()

        return next_move
