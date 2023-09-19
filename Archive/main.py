
import argparse
from tournament import Tournament
from BestRPSAgent import BestRPSAgent
from LLMAgent import LLMAgent
from RandomAgent import RandomAgent
# More agents can be imported as they are refactored

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run a Rock-Paper-Scissors tournament with enhanced LLM interfacing.")
    
    # Add common arguments
    parser.add_argument("--rounds", type=int, default=1000, help="Number of rounds in the tournament.")
    
    # Add LLM interfacing arguments
    parser.add_argument("--format", choices=['plain_text', 'json'], default='plain_text', help="Format of the chat completions.")
    parser.add_argument("--completions", type=int, default=1, help="Number of completions to generate.")
    parser.add_argument("--temperature", type=float, default=1.0, help="Degree of randomness in completions.")
    parser.add_argument("--max_tokens", type=int, default=150, help="Maximum number of tokens in completions.")
    
    args = parser.parse_args()

    print(f"Starting the Rock-Paper-Scissors tournament with {args.rounds} rounds!")
    print(f"LLM Interfacing Options: Format - {args.format}, Completions - {args.completions}, Temperature - {args.temperature}, Max Tokens - {args.max_tokens}")

    # Instantiate agents
    agents = [BestRPSAgent(), LLMAgent(format=args.format, completions=args.completions, temperature=args.temperature, max_tokens=args.max_tokens), RandomAgent()]
    # More agents can be added to this list as they are refactored

    # Instantiate and run the tournament
    rps_tournament = Tournament(agents, num_rounds=args.rounds)
    results = rps_tournament.run_tournament()
    print(results)

if __name__ == "__main__":
    main()
