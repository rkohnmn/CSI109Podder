"""
Author: Robert Thomas Kohn
Date: October 6, 2026
Description: Tournament tracker.
Code of honesty: I have not copied from any source without proper citation.
"""

import random

# variables
tournament_high_score = 0
champion_player = 0

# 10 players
for player_id in range(1, 11):
    print(f"Processing games for Player #{player_id}...")

    # 5 games each
    for game in range(1, 6):
        score = random.randint(1, 1000)

        # check high score
        if score > tournament_high_score:
            tournament_high_score = score
            champion_player = player_id

# print winner
print(f"The tournament champion is Player #{champion_player} with an incredible score of {tournament_high_score}!")
