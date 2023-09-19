import random
from agents import random_agent, best_rps_agent, llm_agent, meta_rps_agent

# COMMENTER ENTITY:
# inquiry: What does this module achieve?
# answer: This module orchestrates the Rock-Paper-Scissors tournament by pitting various agents against each other.

def run_tournament(num_rounds=1000):
    # List of agents participating in the tournament
    agents = [random_agent, best_rps_agent, llm_agent, meta_rps_agent]

    # Track the scores of the agents
    scores = {agent.__name__: 0 for agent in agents}

    # Play the rounds
    for _ in range(num_rounds):
        for i, agent1 in enumerate(agents):
            for j, agent2 in enumerate(agents):
                if i != j:  # An agent doesn't play against itself
                    result = play_round(agent1, agent2)
                    if result == 1:
                        scores[agent1.__name__] += 1
                    elif result == 2:
                        scores[agent2.__name__] += 1

    # PRINT CREATOR ENTITY:
    for agent_name, score in scores.items():
        print(f"{agent_name} scored {score} points in the tournament.")

def play_round(agent1, agent2):
    # COMMENTER ENTITY:
    # inquiry: How do we determine the winner of a round?
    # answer: We use the moves from both agents and compare. The function returns 1 if agent1 wins, 2 if agent2 wins, and 0 for a draw.

    move1 = agent1()
    move2 = agent2()

    # RPS game logic
    if move1 == move2:
        return 0
    if (move1 == "R" and move2 == "S") or (move1 == "S" and move2 == "P") or (move1 == "P" and move2 == "R"):
        return 1
    return 2
