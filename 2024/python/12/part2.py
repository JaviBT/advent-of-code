from collections import defaultdict

raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

if False:
    raw = '''
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''.strip().split('\n')
    raw2 = '''
......CC..
......CCC.
.....CC...
...CCC....
....C..C..
....CC....
.....C....
..........
..........
..........
'''.strip().split('\n')

grid = [[int(char) if char.isdigit() else char for char in line] for line in raw]
n, m = len(grid), len(grid[0])

debug = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
perpendicular_dir = {
                    (-1, 0): [(0, 1), (0, -1)],
                    (1, 0): [(0, 1), (0, -1)],
                    (0, -1): [(1, 0), (-1, 0)],
                    (0, 1): [(1, 0), (-1, 0)]
                }
visited = set()

def calc_area(i, j):
    stack = [(i, j)]
    in_area = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in in_area:
            continue
        in_area.add((x, y))
        visited.add((x, y))

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[i][j]:
                stack.append((nx, ny))
    
    if debug >= 1:print(grid[i][j], len(in_area), "Area")
    return in_area, len(in_area)        

def calc_sides(shape):
    edges = set()
    sides = 0

    for cell in shape:
        x, y = cell
        
        for dx, dy in dir:
            if ((0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] != grid[x][y]) or (not (0 <= x + dx < n and 0 <= y + dy < m))) and (x, y, dx, dy) not in edges:
                if debug >= 2: print((x, y, dx, dy), edges)
                sides += 1
                edge = (x, y, dx, dy)

                current_edge = [edge]
                while current_edge:
                    edge_x, edge_y, edge_dx, edge_dy = current_edge.pop()
                    if grid[edge_x][edge_y] != grid[x][y]:
                        continue
                    edges.add((edge_x, edge_y, edge_dx, edge_dy))
                    
                    for dx2, dy2 in perpendicular_dir[(edge_dx, edge_dy)]:
                        nx, ny = edge_x + dx2, edge_y + dy2
                        if (0 <= nx < n and 0 <= ny < m) and ((0 <= nx + dx < n and 0 <= ny + dy < m and grid[nx + dx][ny + dy] != grid[x][y]) or (not (0 <= nx + dx < n and 0 <= ny + dy < m))) and (nx, ny, dx, dy) not in edges:
                            current_edge.append((nx, ny, dx, dy))

    if debug > 1: print(grid[i][j], sides, "Sides")
    return sides

cnt = 0
for i in range(n):
    for j in range(m):
        if (i, j) in visited:
            continue

        shape, area = calc_area(i, j)
        sides = calc_sides(shape)
        cnt += sides * area

print(cnt)
        