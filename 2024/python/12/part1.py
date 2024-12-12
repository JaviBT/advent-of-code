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

grid = [[int(char) if char.isdigit() else char for char in line] for line in raw]
n, m = len(grid), len(grid[0])

debug = 0
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = set()

def calc_perimeter(i, j):
    stack = [(i, j)]
    
    perimeter = 0
    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] != grid[i][j]:
                perimeter += 1
            else:
                stack.append((nx, ny))
    
    if debug >= 1: print(grid[i][j], perimeter)
    return perimeter

def calc_area(i, j):
    stack = [(i, j)]
    in_area = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in in_area:
            continue
        in_area.add((x, y))

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[i][j]:
                stack.append((nx, ny))
    
    if debug >= 1: print(grid[i][j], len(in_area))
    return len(in_area)        

cnt = 0
for i in range(n):
    for j in range(m):
        if (i, j) in visited:
            continue

        perimeter = calc_perimeter(i, j)
        area = calc_area(i, j)
        cnt += perimeter * area

print(cnt)
        