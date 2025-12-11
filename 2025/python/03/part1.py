import math
raw = open('input.dat').readlines()

total = 0

for line in raw:
    line = line.strip()

    n = len(line)

    first, first_idx = max((int(line[i]), -i) for i in range(n) if i < n - 1)
    second, second_idx = max((int(line[i]), -i) for i in range(n) if i > -first_idx and i < n)

    max_str = str(first) + str(second)
    total += int(max_str)

print(total)
        