num_grid = [[1, 2],
            [3, 4]]

changes = input()
for change in changes:
    if change == "H":
        num_grid[0], num_grid[1] = num_grid[1], num_grid[0]

    if change == "V":
        num_grid[0][0], num_grid[0][1] = num_grid[0][1], num_grid[0][0]
        num_grid[1][0], num_grid[1][1] = num_grid[1][1], num_grid[1][0]

for num in num_grid:
    print(' '.join(map(str, num)))