import math
raw = open('input.dat').readlines()

ranges = []

lines = iter(raw)

for line in lines:
    if line == '\n':
        break
    start, end = line.split('-')[0], line.split('-')[1]
    ranges.append([int(start), int(end)])

ranges.sort(key=lambda x: x[0])

merged_ranges = []

current_start, current_end = ranges[0]
for next_start, next_end in ranges[1:]:
    if next_start <= current_end + 1:
        current_end = max(current_end, next_end)
    else:
        merged_ranges.append([current_start, current_end])
        current_start, current_end = next_start, next_end

merged_ranges.append([current_start, current_end])

total = 0
for start, end in merged_ranges:
    total += end - start + 1

print(total)
