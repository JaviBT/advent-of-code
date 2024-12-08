raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

# Create a 2D Grid from the string input
grid = []
for line in raw:
    row = [char for char in line]
    grid.append(row)

n, m = len(grid), len(grid[0])
visited = set()
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
            visited.add((i, j))
            break

while True:
    cur_dir = grid[x][y]
    dx, dy = dir[cur_dir]
    x, y = x + dx, y + dy

    if x not in range(n) or y not in range(m):
        print(len(visited))
        break

    if grid[x][y] == '#':
        x, y = x - dx, y - dy
        grid[x][y] = symb[cur_dir]
    else:
        grid[x][y] = cur_dir

    visited.add((x, y))
