from agents import random_agent, best_rps_agent, llm_agent, meta_rps_agent

# COMMENTER ENTITY:
# inquiry: What's the main purpose of this rpsrunner module?
# answer: This module provides utility functions to simulate rounds of Rock-Paper-Scissors between different agents, useful for testing their strategies.

def simulate_round(agent1, agent2, num_rounds=1000):
    # Variables to track score
    agent1_score = 0
    agent2_score = 0
    draws = 0

    # Simulate rounds
    for _ in range(num_rounds):
        move1 = agent1()
        move2 = agent2()

        if move1 == move2:
            draws += 1
        elif ((move1 == "R" and move2 == "S") or
              (move1 == "S" and move2 == "P") or
              (move1 == "P" and move2 == "R")):
            agent1_score += 1
        else:
            agent2_score += 1

    return agent1_score, agent2_score, draws

def main():
    # Define agents to test
    agents = [random_agent, best_rps_agent, llm_agent, meta_rps_agent]
    
    # Compare every agent against each other
    for i, agent1 in enumerate(agents):
        for j, agent2 in enumerate(agents):
            if i != j:
                agent1_score, agent2_score, draws = simulate_round(agent1, agent2)
                print(f"{agent1.__name__} vs {agent2.__name__} --> {agent1_score} : {agent2_score} with {draws} draws.")

if __name__ == "__main__":
    main()
