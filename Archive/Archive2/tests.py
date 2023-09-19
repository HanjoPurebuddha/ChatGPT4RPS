
import unittest
from main import llm_move, bestrps_move, RPSGame, random_agent

class TestRPSGame(unittest.TestCase):

    def test_llm_move(self):
        history = []
        # Testing if llm_move function returns one of the valid moves
        self.assertIn(llm_move(history), ['R', 'P', 'S'])

    def test_bestrps_move(self):
        history = []
        # Testing if bestrps_move function returns one of the valid moves
        self.assertIn(bestrps_move(history), ['R', 'P', 'S'])

    def test_random_agent(self):
        history = []
        # Testing if random_agent function returns one of the valid moves
        self.assertIn(random_agent(history), ['R', 'P', 'S'])

    def test_play_round(self):
        game = RPSGame(random_agent, random_agent)
        # Testing if play_round function returns one of the valid outcomes
        self.assertIn(game.play_round(), ['A', 'B', 'Tie'])

    def test_simulate(self):
        game = RPSGame(random_agent, random_agent)
        game.simulate(rounds=10)
        # Testing if simulate function updates the results correctly
        self.assertEqual(sum(game.results.values()), 10)

if __name__ == '__main__':
    unittest.main()
