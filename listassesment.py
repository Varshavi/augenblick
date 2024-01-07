def total_load(grid):
    total_load = 0
    for col in range(len(grid[0])):
        for row in range(len(grid)-1, -1, -1):
            if grid[row][col] == 'O':
                total_load += row + 1
    return total_load

def tilt_platform(grid, direction):
    if direction == 'north':
        return [''.join(row) for row in zip(*grid)]
    elif direction == 'south':
        return [''.join(row) for row in zip(*grid[::-1])][::-1]
    elif direction == 'west':
        return [''.join(row[::-1]) for row in grid]
    elif direction == 'east':
        return [''.join(row) for row in grid[::-1]]

# Your initial grid
grid = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#...."
]

# Tilt the platform north
tilted_grid = tilt_platform(grid, 'north')

# Calculate the total load
result = total_load(tilted_grid)

print("Total load on north support beams:", result)
