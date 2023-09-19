import random

# Constants
BEAT = {'R': 'P', 'P': 'S', 'S': 'R'}
CENTRIFUGE = {'RP': 0, 'PS': 1, 'SR': 2, 'PR': 3, 'SP': 4, 'RS': 5, 'RR': 6, 'PP': 7, 'SS': 8}
CENTRIPETE = {'R': 0, 'P': 1, 'S': 2}
NUM_PRE = 30
NUM_META = 6
LIMIT = 8

def initialize_agent():
    """Initializes and returns the agent's variables."""
    moves = ['', '', '', '']
    p_score = [[5] * NUM_PRE for _ in range(6)]
    soma = [0] * 9
    rps = [1, 1, 1]
    best = [0, 0, 0]
    length = 0
    p = [random.choice("RPS") for _ in range(NUM_PRE)]
    m = [random.choice("RPS") for _ in range(NUM_META)]
    m_score = [5, 2, 5, 2, 4, 2]
    return moves, p_score, soma, rps, best, length, p, m, m_score

def meta_rps_agent(input, output, moves, p_score, soma, rps, best, length, p, m, m_score):
    """Main logic for the meta RPS agent."""
    if not input:
        return initialize_agent()

    for i in range(NUM_PRE):
        pp = p[i]
        bpp = BEAT[pp]
        bbpp = BEAT[bpp]
        p_score[0][i] = 0.9 * p_score[0][i] + ((input == pp) - (input == bbpp)) * 3
        p_score[1][i] = 0.9 * p_score[1][i] + ((output == pp) - (output == bbpp)) * 3
        p_score[2][i] = 0.87 * p_score[2][i] + (input == pp) * 3.3 - (input == bpp) * 1.2 - (input == bbpp) * 2.3
        p_score[3][i] = 0.87 * p_score[3][i] + (output == pp) * 3.3 - (output == bpp) * 1.2 - (output == bbpp) * 2.3
        p_score[4][i] = (p_score[4][i] + (input == pp) * 3) * (1 - (input == bbpp))
        p_score[5][i] = (p_score[5][i] + (output == pp) * 3) * (1 - (output == bbpp))

    for i in range(NUM_META):
        m_score[i] = 0.96 * (m_score[i] + (input == m[i]) - (input == BEAT[BEAT[m[i]]]))

    soma[CENTRIFUGE[input + output]] += 1
    rps[CENTRIPETE[input]] += 1
    moves[0] += str(CENTRIFUGE[input + output])
    moves[1] += input
    moves[2] += output
    length += 1

    for y in range(3):
        j = min([length, LIMIT])
        while j >= 1 and not moves[y][length - j:length] in moves[y][0:length - 1]:
            j -= 1
        i = moves[y].rfind(moves[y][length - j:length], 0, length - 1)
        p[0 + 2 * y] = moves[1][j + i]
        p[1 + 2 * y] = BEAT[moves[2][j + i]]

    return moves, p_score, soma, rps, best, length, p, m, m_score
