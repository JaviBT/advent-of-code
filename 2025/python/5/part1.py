import math
raw = open('input.dat').readlines()

ranges = []
ingredients = []

lines = iter(raw)

for line in lines:
    if line == '\n':
        break
    start, end = line.split('-')[0], line.split('-')[1]
    ranges.append([int(start), int(end)])

for line in lines:
    ingredients.append(int(line))

total = 0
for ingredient in ingredients:
  if any(start <= ingredient <= end for start, end in ranges):
      total += 1

print(total)
