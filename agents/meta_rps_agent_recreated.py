import random

# COMMENTER ENTITY:
# inquiry: What's the strategy for this meta RPS agent?
# answer: This agent attempts to predict the opponent's move based on historical data and patterns, considering both its own moves and the opponent's previous moves.

def meta_rps_agent(prev_play, opponent_history=[]):
    # Maintain the history of plays
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    # For simplicity in this example, the agent will use a basic strategy to counter the opponent's most frequent move.
    move_counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        move_counts[move] += 1

    most_common_move = max(move_counts, key=move_counts.get)
    
    # Counter the most common move
    if most_common_move == "R":
        return "P"
    elif most_common_move == "P":
        return "S"
    else:
        return "R"
