
class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.history = []  # List to store historical moves

    def play_move(self, opponent_move):
        raise NotImplementedError("Each agent must implement the play_move method.")

    def update_history(self, move):
        self.history.append(move)

    def reset_history(self):
        self.history = []
