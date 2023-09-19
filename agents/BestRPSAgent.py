
from .BaseAgent import BaseAgent

class BestRPSAgent(BaseAgent):
    def __init__(self):
        """Initializes the BestRPSAgent by calling the superclass constructor with its name."""
        super().__init__(name="BestRPSAgent")

    def play_move(self, opponent_move: str) -> str:
        """Plays the best counter move based on the opponent's move.
        
        Args:
            opponent_move (str): The move played by the opponent.
            
        Returns:
            str: The best counter move.
        """
        if opponent_move == "R":
            return "P"
        elif opponent_move == "P":
            return "S"
        elif opponent_move == "S":
            return "R"
        else:
            raise ValueError(f"Invalid opponent move: {opponent_move}")
