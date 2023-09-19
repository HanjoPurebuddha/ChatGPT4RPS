# tests.py
#
# This module contains tests to validate the functionality of the Rock-Paper-Scissors
# simulation application. It ensures that the agents and game mechanics are correctly implemented.

from RPSGame import RPSGame
from LLMAgent import llm_move
from bestrps import bestrps_move

def test_llm_agent():
    """ Test the functionality of the LLM agent. """
    assert llm_move() in ["R", "P", "S"]

def test_bestrps_agent():
    """ Test the functionality of the bestrps agent. """
    assert bestrps_move() in ["R", "P", "S"]

def test_game_simulation():
    """ Test the game simulation between two agents. """
    game = RPSGame(llm_move, bestrps_move)
    game.simulate(100)
    assert sum(game.results.values()) == 100

def test_llm_strategy():
    """ Test if the LLM strategy identifies patterns. """
    history = [("R", "P"), ("R", "P"), ("R", "P")]
    # Given the pattern, LLM should play S to counter expected R from opponent
    assert llm_move(history) == "S"

def test_invalid_moves():
    """ Test the game's response to irregular patterns in history. """
    game = RPSGame(llm_move, bestrps_move)
    game.history = [("R", "X"), ("R", "Y"), ("R", "Z")]
    game.simulate_round()  # This should not raise any errors

def run_all_tests():
    """ Run all the tests and report the results. """
    test_llm_agent()
    test_bestrps_agent()
    test_game_simulation()
    test_llm_strategy()
    test_invalid_moves()
    print("All tests passed!")

if __name__ == "__main__":
    run_all_tests()
