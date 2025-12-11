import math
import time

raw = open('input.dat').readlines()

grid = []

lines = raw
for line in lines:
    grid.append([x for x in line])

start = None
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == 'S':
            start = (r, c)
            break
    if start:
        break

beams = {start}
splits = 0
n = len(grid)

while beams:
    next_beams = set()
    for r, c in beams:
        if r >= n:
            continue
        
        nr = r + 1
        if nr >= n:
            continue
            
        new_tile = grid[nr][c]
        
        if new_tile == '^':
            splits += 1
            
            if c - 1 >= 0:
                next_beams.add((nr, c - 1))
            if c + 1 < len(grid[nr]):
                next_beams.add((nr, c + 1))
        else:
            next_beams.add((nr, c))
            
    beams = next_beams

print(splits)
