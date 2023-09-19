from agents.LLMAgent import LLMAgent
from agents.BestRPSAgent import BestRPSAgent
from agents.RandomAgent import RandomAgent
from agents.BaseAgent import BaseAgent

def run_tournament(chosen_agent: BaseAgent) -> tuple:
    wins, losses, ties = 0, 0, 0
    for _ in range(1000):  # Running a best-of-1000 contest
        try:
            move = chosen_agent.play_move()
            if move not in ["R", "P", "S"]:
                print(f"Bot {chosen_agent.name} disqualified due to invalid move: {move}")
                losses += 1
                continue
            opponent_move = "R"  # Placeholder move for opponent
            if move == opponent_move:
                ties += 1
            elif (move == "R" and opponent_move == "S") or \
                 (move == "P" and opponent_move == "R") or \
                 (move == "S" and opponent_move == "P"):
                wins += 1
            else:
                losses += 1
        except Exception as e:
            print(f"Bot {chosen_agent.name} encountered an error: {e}")
            losses += 1
    return wins, losses, ties

def display_results(wins: int, losses: int, ties: int) -> None:
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Ties: {ties}")

def main():
    agents = [LLMAgent(), BestRPSAgent(), RandomAgent()]
    print("Welcome to the RPS Tournament!")
    print("Available agents are:")
    for i, agent in enumerate(agents, 1):
        print(f"{i}. {agent.name}")
    choice = int(input("Choose an agent by entering its corresponding number: "))
    chosen_agent = agents[choice-1]
    wins, losses, ties = run_tournament(chosen_agent)
    display_results(wins, losses, ties)

# If this script is the main module, run the main function
if __name__ == "__main__":
    main()