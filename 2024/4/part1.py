import re

raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

n, m = len(raw), len(raw[0])

def check_horizontal(i, j):
    count = 0
    # Check rightward (XMAS →)
    if j + 3 < m:
        if raw[i][j] == 'X' and raw[i][j + 1] == 'M' and raw[i][j + 2] == 'A' and raw[i][j + 3] == 'S':
            count += 1
    # Check leftward (SAMS ←)
    if j - 3 >= 0:
        if raw[i][j] == 'X' and raw[i][j - 1] == 'M' and raw[i][j - 2] == 'A' and raw[i][j - 3] == 'S':
            count += 1
    return count

def check_vertical(i, j):
    count = 0
    # Check downward (XMAS ↓)
    if i + 3 < n:
        if raw[i][j] == 'X' and raw[i + 1][j] == 'M' and raw[i + 2][j] == 'A' and raw[i + 3][j] == 'S':
            count += 1
    # Check upward (SAMS ↑)
    if i - 3 >= 0:
        if raw[i][j] == 'X' and raw[i - 1][j] == 'M' and raw[i - 2][j] == 'A' and raw[i - 3][j] == 'S':
            count += 1
    return count


def check_diagonal(i, j):
    count = 0
    # Check diagonal downward-right (XMAS ↘)
    if i + 3 < n and j + 3 < m:
        if raw[i][j] == 'X' and raw[i + 1][j + 1] == 'M' and raw[i + 2][j + 2] == 'A' and raw[i + 3][j + 3] == 'S':
            count += 1
    # Check diagonal upward-left (SAMS ↖)
    if i - 3 >= 0 and j - 3 >= 0:
        if raw[i][j] == 'X' and raw[i - 1][j - 1] == 'M' and raw[i - 2][j - 2] == 'A' and raw[i - 3][j - 3] == 'S':
            count += 1
    # Check diagonal downward-left (XMAS ↙)
    if i + 3 < n and j - 3 >= 0:
        if raw[i][j] == 'X' and raw[i + 1][j - 1] == 'M' and raw[i + 2][j - 2] == 'A' and raw[i + 3][j - 3] == 'S':
            count += 1
    # Check diagonal upward-right (SAMS ↗)
    if i - 3 >= 0 and j + 3 < m:
        if raw[i][j] == 'X' and raw[i - 1][j + 1] == 'M' and raw[i - 2][j + 2] == 'A' and raw[i - 3][j + 3] == 'S':
            count += 1
    return count


def check_all(i, j):
    return check_horizontal(i, j) + check_vertical(i, j) + check_diagonal(i, j)

cnt = 0
for i, row in enumerate(raw):
    for j, col in enumerate(row):
        cnt += check_all(i, j)

print(cnt)
