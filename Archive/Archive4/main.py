
from agents.BaseAgent import BaseAgent
from agents.RandomAgent import RandomAgent
from agents.BestRPSAgent import BestRPSAgent
from agents.LLMAgent import LLMAgent
import openai

def run_tournament(agents: list[BaseAgent], rounds: int = 100):
    """Execute a tournament where each agent plays against every other agent.
    
    Args:
        agents (list[BaseAgent]): List of agents participating in the tournament.
        rounds (int): Number of rounds each agent pair will play. Default is 100.
    """
    for i, agent1 in enumerate(agents):
        for j, agent2 in enumerate(agents):
            if i != j:
                for _ in range(rounds):
                    move1 = agent1.play_move()
                    move2 = agent2.play_move()
                    # TODO: Implement the logic to determine the winner and update scores

if __name__ == "__main__":
    # Define the API key for LLMAgent
    api_key = "YOUR_OPENAI_API_KEY"
    
    # Instantiate the agents
    random_agent = RandomAgent()
    best_rps_agent = BestRPSAgent()
    llm_agent = LLMAgent(api_key=api_key)
    
    # List of agents
    agents = [random_agent, best_rps_agent, llm_agent]
    
    # Execute the tournament
    run_tournament(agents)
