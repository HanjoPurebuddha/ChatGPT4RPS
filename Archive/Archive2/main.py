import argparse
import tournament

# COMMENTER ENTITY:
# inquiry: What is the main purpose of this module?
# answer: This module serves as the command-line interface (CLI) for running the Rock-Paper-Scissors tournament.

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run a Rock-Paper-Scissors tournament.")
    
    # Add arguments
    parser.add_argument("--rounds", type=int, default=1000, help="Number of rounds in the tournament.")
    args = parser.parse_args()

    # PRINT CREATOR ENTITY:
    print(f"Starting the Rock-Paper-Scissors tournament with {args.rounds} rounds!")

    # Run the tournament
    tournament.run_tournament(num_rounds=args.rounds)

if __name__ == "__main__":
    main()
