import random

# COMMENTER ENTITY:
# inquiry: What's the strategy behind this agent?
# answer: This agent tries to predict the opponent's next move based on their last move and counters it.

def best_rps_agent(prev_play, opponent_history=[]):
    # If no previous play is available, default to a random move
    if prev_play is None:
        return random.choice(["R", "P", "S"])

    # Based on the previous play, make a prediction for the next move
    if prev_play == "R":
        next_move = "P"
    elif prev_play == "P":
        next_move = "S"
    else:
        next_move = "R"

    # PRINT CREATOR ENTITY:
    print(f"Best RPS Agent predicts opponent's move as {prev_play} and counters with {next_move}.")

    return next_move
