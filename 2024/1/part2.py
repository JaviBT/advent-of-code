# Read the input.dat each line has to values one for the left list and one for the right list
raw = open('input.dat').readlines()

l, r = [], []
for line in raw:
    l.append(int(line.split()[0]))
    r.append(int(line.split()[1]))

feq_r = {}
for num in r:
    feq_r[num] = feq_r.get(num, 0) + 1

similarity_score = 0
for num in l:
    similarity_score += num * feq_r.get(num, 0)

print(similarity_score)
