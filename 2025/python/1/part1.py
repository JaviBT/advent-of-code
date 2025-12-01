raw = open('input.dat').readlines()

count = 0
dial = 50

for line in raw:
    line = line.strip()
    if not line: continue
    move = int(line[1:])
    if line[0] == 'L':
        dial = (dial - move) % 100
    elif line[0] == 'R':
        dial = (dial + move) % 100
    if dial == 0:
        count += 1
        
print(count)
