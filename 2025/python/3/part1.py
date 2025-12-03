import math
raw = open('input.dat').readlines()

total = 0

for line in raw:
    line = line.strip()

    first, first_idx = max((int(line[i]), i) for i in range(len(line)))
    second, second_idx = max((int(line[i]), i) for i in range(len(line)) if i >= first_idx)

    total += int(str(first) + str(second))

print(total)
        