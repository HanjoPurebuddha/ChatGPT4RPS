import os
from rpsrunner import run_tournament

def main():
    """
    Main function to run the RPS Tournament.
    """
    os.system('clear')
    print("Welcome to the RPS Tournament!")
    
    # Run the tournament
    run_tournament()

if __name__ == "__main__":
    main()
