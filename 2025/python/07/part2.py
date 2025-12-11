import math
import time
from collections import defaultdict

raw = open('input.dat').readlines()

grid = []

lines = raw
for line in lines:
    grid.append([x for x in line.strip()])

start = None
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 'S':
            start = (r, c)
            break
    if start:
        break

if not start:
    print(0)
    exit()

beams = {start: 1}
splits = 0
n = len(grid)

while beams:
    next_beams = defaultdict(int)
    for (r, c), count in beams.items():
        nr = r + 1
        if nr >= n:
            splits += count
            continue
            
        if c >= len(grid[nr]):
            splits += count
            continue

        new_tile = grid[nr][c]
        
        if new_tile == '^':
            if c - 1 >= 0:
                next_beams[(nr, c - 1)] += count
            else:
                splits += count
            
            if c + 1 < len(grid[nr]):
                next_beams[(nr, c + 1)] += count
            else:
                splits += count
        else:
            next_beams[(nr, c)] += count
            
    beams = next_beams

print(splits)
