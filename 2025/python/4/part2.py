import math
raw = open('input.dat').readlines()

grid = [[x for x in line.strip()] for line in raw]

def checkKAdjacent(grid, x, y, k):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    khits = 0
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '@':
            khits += 1
    return khits >= k

total = 0
last_iter = -1

while last_iter != 0:
    last_iter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@' and not checkKAdjacent(grid, i, j, 4):
                grid[i][j] = '.'
                last_iter += 1
                total += 1

print(total)
