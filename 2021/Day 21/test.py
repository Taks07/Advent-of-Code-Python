import functools
from itertools import product

QUANTUM_ROLLS = tuple(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))
@functools.cache
def play2(my_pos, my_score, other_pos, other_score):
    if my_score >= 21:
        return 1, 0

    if other_score >= 21:
        return 0, 1

    my_wins = other_wins = 0

    for roll in QUANTUM_ROLLS:
        # Play one turn calculating the new score with the current roll:
        new_pos   = (my_pos + roll) % 10
        new_score = my_score + new_pos + 1

        # Let the other player play, swapping the arguments:
        ow, mw = play2(other_pos, other_score, new_pos, new_score)

        # Update total wins of each player:
        my_wins    += mw
        other_wins += ow

    return my_wins, other_wins

wins = play2(3, 0, 7, 0)
best = max(wins)

print('Part 2:', best)