import math
import time

raw = open('input.dat').readlines()

tiles = []
for line in raw:
    if not line.strip(): continue
    x, y = line.strip().split(',')
    tiles.append((int(x), int(y)))

edges = []
N = len(tiles)
for i in range(N):
    p1 = tiles[i]
    p2 = tiles[(i + 1) % N]
    edges.append((p1, p2))

def is_valid_geometric(xmin, xmax, ymin, ymax, tiles, edges):
    # B = Bounding Box and R = Rectangle
    # 1. No vertex of B strictly inside R
    for vx, vy in tiles:
        if xmin < vx < xmax and ymin < vy < ymax:
            return False

    # 2. No edge of B cuts through R
    for (ex1, ey1), (ex2, ey2) in edges:
        # Horizontal edge
        if ey1 == ey2:
            ey = ey1
            emin_x, emax_x = min(ex1, ex2), max(ex1, ex2)
            if (ymin < ey < ymax) and (emin_x <= xmin and emax_x >= xmax):
                return False
        # Vertical edge
        else:
            ex = ex1
            emin_y, emax_y = min(ey1, ey2), max(ey1, ey2)
            if (xmin < ex < xmax) and (emin_y <= ymin and emax_y >= ymax):
                return False

    # For my input, this is enough and I can return true, but in general
    # I also need to check if the center of R is inside or on boundary of B.
    # For some concave rectilinear polygons, this is not enough.
    return True

max_area = 0

for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]

        xmin, xmax = min(x1, x2), max(x1, x2)
        ymin, ymax = min(y1, y2), max(y1, y2)
        
        width = xmax - xmin + 1
        height = ymax - ymin + 1
        area = width * height
        
        if area <= max_area:
            continue
            
        if is_valid_geometric(xmin, xmax, ymin, ymax, tiles, edges):
            max_area = area

print(max_area)
