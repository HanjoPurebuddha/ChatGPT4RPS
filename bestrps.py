def bestrps_play(history):
    """
    An agent that plays the Rock-Paper-Scissors game.
    This agent makes decisions based on the history of the opponent's moves.
    """
    if not history or len(history['player2']) < 3:
        return random.choice(['R', 'P', 'S'])
    
    # Count the opponent's moves in the last three rounds
    last_three_moves = history['player2'][-3:]
    move_counts = {'R': last_three_moves.count('R'), 'P': last_three_moves.count('P'), 'S': last_three_moves.count('S')}
    
    # Choose the move that beats the opponent's most frequent move in the last three rounds
    if move_counts['R'] > move_counts['P'] and move_counts['R'] > move_counts['S']:
        return 'P'  # Paper covers rock
    elif move_counts['P'] > move_counts['R'] and move_counts['P'] > move_counts['S']:
        return 'S'  # Scissors cut paper
    else:
        return 'R'  # Rock crushes scissors
