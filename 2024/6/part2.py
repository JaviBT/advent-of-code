from copy import deepcopy
from tqdm import tqdm

raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

# Create a 2D Grid from the string input
grid = []
for line in raw:
    row = [char for char in line]
    grid.append(row)

n, m = len(grid), len(grid[0])
dir = {
    '^': (-1, 0),
    'v': (1, 0),
    '>': (0, 1),
    '<': (0, -1)
}
symb = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

for i in range(n):
    for j in range(m):
        if grid[i][j] == '^':
            x, y = i, j
            break

def simulate(grid, x, y):
    visited = set()
    path = set()

    while True:
        cur_dir = grid[x][y]
        
        if (x, y, cur_dir) in path:
            return True
        path.add((x, y, cur_dir))
        visited.add((x, y))

        dx, dy = dir[cur_dir]
        x, y = x + dx, y + dy

        if x not in range(n) or y not in range(m):
            return False

        if grid[x][y] == '#':
            x, y = x - dx, y - dy
            grid[x][y] = symb[cur_dir]
        else:
            grid[x][y] = cur_dir

valid_positions = 0
for i in tqdm(range(n)):
    for j in range(m):
        if grid[i][j] == '.' and (i, j) != (x, y):
            temp_grid = deepcopy(grid)
            temp_grid[i][j] = '#'

            if simulate(temp_grid, x, y):
                valid_positions += 1

print(valid_positions)
