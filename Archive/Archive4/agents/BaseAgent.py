
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name: str):
        """Initializes the BaseAgent with a given name and an empty move history.
        
        Args:
            name (str): Name of the agent.
        """
        self.name = name
        self.history = []

    @abstractmethod
    def play_move(self) -> str:
        """Abstract method to play a move. Derived agents must implement this method.
        
        Returns:
            str: The move played by the agent.
        """
        pass

    def update_history(self, move: str):
        """Updates the agent's move history with the provided move.
        
        Args:
            move (str): The move to be added to the agent's history.
        """
        self.history.append(move)

    def reset_history(self):
        """Resets the agent's move history."""
        self.history = []
