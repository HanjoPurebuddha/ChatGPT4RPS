
from .BaseAgent import BaseAgent
import random

class RandomAgent(BaseAgent):
    def __init__(self):
        """Initializes the RandomAgent by calling the superclass constructor with its name."""
        super().__init__(name="RandomAgent")

    def play_move(self, opponent_move=None) -> str:
        """Selects a random move from the list of possible moves and returns it.
        
        Args:
            opponent_move (str, optional): The move played by the opponent. Defaults to None.
            
        Returns:
            str: The move selected by the RandomAgent.
        """
        return random.choice(["R", "P", "S"])
