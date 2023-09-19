
import random

class RandomAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="RandomAgent")

    def play_move(self, opponent_move=None):
        return random.choice(["R", "P", "S"])
