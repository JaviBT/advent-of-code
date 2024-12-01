# Read the input.dat each line has to values one for the left list and one for the right list
raw = open('input.dat').readlines()

l, r = [], []
for line in raw:
    l.append(int(line.split()[0]))
    r.append(int(line.split()[1]))

l.sort()
r.sort()

diff = 0
for i in range(len(l)):
    diff += abs(l[i] - r[i])

print(diff)
