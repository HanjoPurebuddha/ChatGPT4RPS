import random
from bestrps import bestrps_play
from LLMagent import llm_play
from meta_rps_agent import output as meta_rps_play

def run_game(player1, player2, num_rounds=1000):
    """
    Run the RPS game between two players for a certain number of rounds.
    Returns the results of the game.
    """
    score = {"player1": 0, "player2": 0, "tie": 0}
    history = {"player1": [], "player2": []}
    
    for _ in range(num_rounds):
        move1 = player1(history)
        move2 = player2(history)
        
        history["player1"].append(move1)
        history["player2"].append(move2)
        
        if move1 == move2:
            score["tie"] += 1
        elif (move1 == "R" and move2 == "S") or (move1 == "S" and move2 == "P") or (move1 == "P" and move2 == "R"):
            score["player1"] += 1
        else:
            score["player2"] += 1
    
    return score

def run_tournament():
    """
    Run the RPS tournament between multiple players.
    """
    players = [bestrps_play, llm_play, meta_rps_play]
    results = {}
    
    for i, player1 in enumerate(players):
        for j, player2 in enumerate(players):
            if i != j:
                result = run_game(player1, player2)
                results[f"player{i+1}_vs_player{j+1}"] = result
    
    for match, result in results.items():
        print(f"\nResults for {match}:")
        print(f"Player1: {result['player1']}, Player2: {result['player2']}, Ties: {result['tie']}")

