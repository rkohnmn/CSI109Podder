"""
Author: Robert Thomas Kohn
Date: October 19, 2026
Description: Traverses a 2D elevation grid to locate highest and lowest points, calculates global and per-row averages, and analyzes local neighbour steepness.
Code of honesty: I have not copied from any source without proper citation.
"""

# Part 3: Two-Dimensional List Traversal
# Row 0 is the top row; column 0 is the leftmost column
elevation_grid = [
    [20, 21, 22, 23, 24, 25],
    [21, 25, 26, 24, 23, 26],
    [22, 27, 29, 28, 26, 27],
    [23, 28, 32, 31, 29, 28],
    [24, 26, 30, 33, 31, 29],
    [25, 25, 28, 31, 30, 28]
]

# Task 1: Find highest and lowest elevations with coordinates using nested loops
highest_val = elevation_grid[0][0]
highest_coord = (0, 0)
lowest_val = elevation_grid[0][0]
lowest_coord = (0, 0)

total_elevation = 0
total_cells = 0

for r in range(len(elevation_grid)):
    for c in range(len(elevation_grid[r])):
        current_val = elevation_grid[r][c]
        total_elevation += current_val
        total_cells += 1

        if current_val > highest_val:
            highest_val = current_val
            highest_coord = (r, c)

        if current_val < lowest_val:
            lowest_val = current_val
            lowest_coord = (r, c)

print(f"Highest: {highest_val} at {highest_coord}")
print(f"Lowest: {lowest_val} at {lowest_coord}")

# Task 2: Overall grid average
overall_avg = total_elevation / total_cells
print(f"Average elevation: {overall_avg:.2f}")

# Task 3: Calculate each row's average and identify the highest row average
highest_row_idx = 0
highest_row_avg = sum(elevation_grid[0]) / len(elevation_grid[0])

for r in range(len(elevation_grid)):
    row_avg = sum(elevation_grid[r]) / len(elevation_grid[r])
    print(f"Row {r}: {row_avg:.2f}")
    if row_avg > highest_row_avg:
        highest_row_avg = row_avg
        highest_row_idx = r

print(f"Highest row on average: row {highest_row_idx} ({highest_row_avg:.2f})")

# Part 4 (Bonus / Early Finish): Steepness check around cell (2, 2)
current_r, current_c = 2, 2
center_elev = elevation_grid[current_r][current_c]

neighbours = [
    ("Up", (current_r - 1, current_c)),
    ("Down", (current_r + 1, current_c)),
    ("Left", (current_r, current_c - 1)),
    ("Right", (current_r, current_c + 1))
]

print(f"\nSteepness check from cell ({current_r}, {current_c}) with elevation {center_elev}:")
smoothest_label = ""
smoothest_coord = None
min_diff = None

for label, (nr, nc) in neighbours:
    n_elev = elevation_grid[nr][nc]
    diff = abs(n_elev - center_elev)
    print(f"{label} {nr, nc}: elevation {n_elev}, difference {diff}")
    if min_diff is None or diff < min_diff:
        min_diff = diff
        smoothest_label = label
        smoothest_coord = (nr, nc)

print(f"Smoothest step: {smoothest_label} at {smoothest_coord} with difference {min_diff}")
