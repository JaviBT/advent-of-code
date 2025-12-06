import math
raw = open('input.dat').readlines()

lines = raw

max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) for line in lines]

rows = lines[:-1]

cols = []
for c in range(max_len):
    col_str = ''.join(row[c] for row in rows)
    cols.append(col_str)

numbers = []
new_numbers = []
for c in range(max_len):
    col = cols[c]
    if col.strip() == '':
        numbers.append(new_numbers)
        new_numbers = []
    else:
        new_numbers.append(int(col))
if new_numbers:
    numbers.append(new_numbers)

operators = lines[-1].split()

total = 0
for i, curNums in enumerate(numbers):
  if operators[i] == '*':
    curSum = 1
    for j in range(len(curNums)):
      curSum *= curNums[j]
  elif operators[i] == '+':
    curSum = 0
    for j in range(len(curNums)):
      curSum += curNums[j]
  total += curSum

print(total)
