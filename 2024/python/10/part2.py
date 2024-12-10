raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

if False:
    raw = '''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''
    raw = raw.strip().split('\n')

grid = [[int(char) if char.isdigit() else char for char in line] for line in raw]
n, m = len(grid), len(grid[0])

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def calc_trailheads(grid, i, j):
    if (grid[i][j] == 9):
        return 1
    if (grid[i][j] == '.'):
        return 0
    
    score = 0
    for dx, dy in dir:
        if i + dx in range(n) and j + dy in range(m) and grid[i + dx][j + dy] == grid[i][j] + 1:
            score += calc_trailheads(grid, i + dx, j + dy)
    
    return score


score = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            score += calc_trailheads(grid, i, j)

print(score)
