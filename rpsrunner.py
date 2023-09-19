
import os
import sys
import random
import multiprocessing

# Function to load a bot from a specified file
def load_bot(filename):
    with open(filename, 'r') as file:
        code = compile(file.read(), filename, 'exec')
    bot_namespace = {}
    exec(code, bot_namespace)
    return bot_namespace['move']

# Function to play a match between two bots
def play_match(bot_a, bot_b, num_games=1000):
    history = {"A": [], "B": []}
    score = {"A": 0, "B": 0, "Tie": 0}
    for _ in range(num_games):
        move_a = bot_a(history["B"], history["A"])
        move_b = bot_b(history["A"], history["B"])
        history["A"].append(move_a)
        history["B"].append(move_b)

        if move_a == move_b:
            score["Tie"] += 1
        elif (move_a == "R" and move_b == "S") or (move_a == "P" and move_b == "R") or (move_a == "S" and move_b == "P"):
            score["A"] += 1
        else:
            score["B"] += 1
    return score

# Function to run a series of matches in parallel
def run_matches(bots, num_games=1000, num_processes=4):
    pool = multiprocessing.Pool(processes=num_processes)
    results = []

    for i, bot_a in enumerate(bots):
        for j, bot_b in enumerate(bots):
            if i < j:
                result = pool.apply_async(play_match, (bot_a, bot_b, num_games))
                results.append(result)
    
    pool.close()
    pool.join()

    for result in results:
        print(result.get())

# Main function to initiate the bot matches
def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <bot_file_1> <bot_file_2> [<bot_file_3> ...]")
        sys.exit(1)
    
    bot_files = sys.argv[1:]
    bots = [load_bot(bot_file) for bot_file in bot_files]
    run_matches(bots)

if __name__ == "__main__":
    main()
