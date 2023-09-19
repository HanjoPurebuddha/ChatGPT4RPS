import random
from LLMagent import llm_move
from bestrps import bestrps_move

class RPSGame:
    def __init__(self, agent_a_move_func, agent_b_move_func):
        self.agent_a_move_func = agent_a_move_func
        self.agent_b_move_func = agent_b_move_func
        self.history = []
        self.results = {"A": 0, "B": 0, "Tie": 0}

    def play_round(self):
        move_a = self.agent_a_move_func(self.history)
        move_b = self.agent_b_move_func(self.history)
        self.history.append((move_a, move_b))

        if move_a == move_b:
            self.results["Tie"] += 1
            return "Tie"
        elif (move_a == "R" and move_b == "S") or (move_a == "S" and move_b == "P") or (move_a == "P" and move_b == "R"):
            self.results["A"] += 1
            return "A"
        else:
            self.results["B"] += 1
            return "B"

    def simulate(self, rounds=1000):
        for _ in range(rounds):
            self.play_round()

    def report(self):
        total_games = sum(self.results.values())
        report_str = f"After {{total_games}} games:\\n"
        report_str += f"Agent A wins: {{self.results['A']}} games\\n"
        report_str += f"Agent B wins: {{self.results['B']}} games\\n"
        report_str += f"Ties: {{self.results['Tie']}} games"
        return report_str

def random_agent(history):
    return random.choice(["R", "P", "S"])

def main():
    game = RPSGame(llm_move, bestrps_move)
    game.simulate()
    print(game.report())

if __name__ == "__main__":
    main()