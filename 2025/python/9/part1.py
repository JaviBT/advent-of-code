import math
import time

raw = open('input.dat').readlines()

tiles = []
for line in raw:
    if not line.strip(): continue
    x, y = line.strip().split(',')
    tiles.append((int(x), int(y)))

max_area = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        
        width = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        area = width * height
        
        if area > max_area:
            max_area = area

print(max_area)
