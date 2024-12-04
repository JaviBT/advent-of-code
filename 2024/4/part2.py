import re

raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

n, m = len(raw), len(raw[0])

def check_x_mas(i, j):
    # Ensure the current position has an 'A'
    if raw[i][j] != 'A':
        return 0
    
    # Check diagonals
    top_left = (i - 1, j - 1)
    bottom_right = (i + 1, j + 1)
    top_right = (i - 1, j + 1)
    bottom_left = (i + 1, j - 1)
    
    # First diagonal ↘ (top-left to bottom-right)
    has_m_s_diagonal1 = (
        (0 <= top_left[0] < n and 0 <= top_left[1] < m and raw[top_left[0]][top_left[1]] == 'M' and
         0 <= bottom_right[0] < n and 0 <= bottom_right[1] < m and raw[bottom_right[0]][bottom_right[1]] == 'S') or
        (0 <= top_left[0] < n and 0 <= top_left[1] < m and raw[top_left[0]][top_left[1]] == 'S' and
         0 <= bottom_right[0] < n and 0 <= bottom_right[1] < m and raw[bottom_right[0]][bottom_right[1]] == 'M')
    )
    
    # Second diagonal ↙ (top-right to bottom-left)
    has_m_s_diagonal2 = (
        (0 <= top_right[0] < n and 0 <= top_right[1] < m and raw[top_right[0]][top_right[1]] == 'M' and
         0 <= bottom_left[0] < n and 0 <= bottom_left[1] < m and raw[bottom_left[0]][bottom_left[1]] == 'S') or
        (0 <= top_right[0] < n and 0 <= top_right[1] < m and raw[top_right[0]][top_right[1]] == 'S' and
         0 <= bottom_left[0] < n and 0 <= bottom_left[1] < m and raw[bottom_left[0]][bottom_left[1]] == 'M')
    )
    
    # If both diagonals form valid crosses, return 1
    return 1 if has_m_s_diagonal1 and has_m_s_diagonal2 else 0

cnt = 0
for i, row in enumerate(raw):
    for j, col in enumerate(row):
        cnt += check_x_mas(i, j)

print(cnt)
