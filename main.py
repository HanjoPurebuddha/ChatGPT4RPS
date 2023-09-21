import csv
from agents.LLMAgent import LLMAgent
from agents.BestRPSAgent import BestRPSAgent
from agents.RandomAgent import RandomAgent
from agents.BaseAgent import BaseAgent


def run_tournament(chosen_agent: BaseAgent) -> dict:
    results = {"wins": 0, "losses": 0, "ties": 0, "details": []}
    opponents = [LLMAgent(), BestRPSAgent(), RandomAgent()]
    opponents.remove(chosen_agent)

    for opponent in opponents:
        for _ in range(1000):
            try:
                move = chosen_agent.play_move()
                opp_move = opponent.play_move()
                if move == opp_move:
                    results["ties"] += 1
                    result = "Tie"
                elif (move == "R" and opp_move == "S") or \
                        (move == "P" and opp_move == "R") or \
                        (move == "S" and opp_move == "P"):
                    results["wins"] += 1
                    result = "Win"
                else:
                    results["losses"] += 1
                    result = "Loss"
                match_detail = {
                    "opponent": opponent.name,
                    "chosen_move": move,
                    "opponent_move": opp_move,
                    "result": result
                }
                results["details"].append(match_detail)
            except Exception as e:
                print(f"Bot {chosen_agent.name} encountered an error: {e}")
                results["losses"] += 1
    return results


def output_to_csv(results: dict, agent_name: str) -> None:
    with open(f"{agent_name}_tournament_results.csv", "w", newline='') as csvfile:
        fieldnames = ["opponent", "chosen_move", "opponent_move", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for match in results["details"]:
            writer.writerow(match)
    print(f"Results saved to {agent_name}_tournament_results.csv")


def main():
    agents = [LLMAgent(), BestRPSAgent(), RandomAgent()]
    print("Welcome to the RPS Tournament!")
    print("Available agents are:")
    for i, agent in enumerate(agents, 1):
        print(f"{i}. {agent.name}")
    choice = int(input("Choose an agent by entering its corresponding number: "))
    chosen_agent = agents[choice - 1]
    results = run_tournament(chosen_agent)
    output_to_csv(results, chosen_agent.name)


# If this script is the main module, run the main function
if __name__ == "__main__":
    main()