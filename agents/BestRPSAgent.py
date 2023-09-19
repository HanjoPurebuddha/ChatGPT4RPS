
class BestRPSAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="BestRPSAgent")

    def play_move(self, opponent_move):
        if opponent_move == "Rock":
            return "Paper"
        elif opponent_move == "Paper":
            return "Scissors"
        elif opponent_move == "Scissors":
            return "Rock"
        else:
            return "Rock"
