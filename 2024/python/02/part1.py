# Read the input.dat each line has to values one for the left list and one for the right list
raw = open('input.dat').readlines()

cnt = 0
for report in raw:
    levels = [int(x) for x in report.split()]
    
    safe = True
    monotoneus = ''
    for i in range(1, len(levels)):
        if abs(levels[i] - levels[i  - 1]) == 0 or abs(levels[i] - levels[i  - 1]) > 3 \
            or monotoneus == 'des' and levels[i  - 1] < levels[i] \
            or monotoneus == 'asc' and levels[i  - 1] > levels[i]:
            safe = False
            break
        else:
            monotoneus = 'asc' if levels[i  - 1] < levels[i] else 'des'
    
    if safe:
        cnt += 1

print(cnt)
