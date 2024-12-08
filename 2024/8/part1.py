raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

grid = [[char for char in line] for line in raw]
n, m = len(grid), len(grid[0])

if False:
    example = '''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''
    
    grid = [list(line) for line in example.strip().split('\n')]
    n, m = len(grid), len(grid[0])

    print(grid)

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calc_antinodes(a, b, n, m):
    antinodes_set = set()
    ax, ay = a
    bx, by = b

    dx = bx - ax
    dy = by - ay

    for i in range(n):
        for j in range(m):
            if ((i - ax) * (by - ay) == (j - ay) * (bx - ax)) and \
                ((distance((i, j), (ax, ay)) == 2 * distance((i, j), (bx, by))) or \
                (distance((i, j), (bx, by)) == 2 * distance((i, j), (ax, ay)))):
                antinodes_set.add((i, j))

    return antinodes_set

antinodes = set()
antenas = {}
for i in range(n):
    for j in range(m):
        symb = grid[i][j]
        if symb != '.':
            if symb not in antenas:
                antenas[symb] = []

            for pair in antenas[symb]:
                antinodes_set = calc_antinodes((i, j), pair, n, m)
                antinodes = antinodes.union(antinodes_set)

            antenas[symb].append((i, j))

# Plot the grid with all the antinodes
for i in range(n):
    for j in range(m):
        if (i, j) in antinodes:
            grid[i][j] = '#'

for line in grid:
    print(''.join(line))


print(len(antinodes))
