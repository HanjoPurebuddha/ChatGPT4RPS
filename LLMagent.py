
def llm_move(history):
    def llm_move(history=None):
    """ 
    Determine the move for the LLM agent.
    
    Parameters:
    - history (list): List of tuples representing past moves. Each tuple is in the form 
                     (LLM_move, opponent_move). Default is None.
    
    Returns:
    - str: The chosen move ("R", "P", or "S").
    """
    
    if history and len(history) > 2:
        # Check the last three moves of the opponent
        last_three_moves = [move[1] for move in history[-3:]]
        
        # If the opponent has a consistent pattern, predict and counter it
        if len(set(last_three_moves)) == 1:
            if last_three_moves[0] == "R":
                return "P"
            elif last_three_moves[0] == "P":
                return "S"
            else:
                return "R"
    
    # If no pattern detected or history is too short, make a random choice
    return random.choice(["R", "P", "S"])
