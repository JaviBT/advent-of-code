import math
raw = open('input.dat').readlines()

total = 0

for line in raw:
    line = line.strip()
    
    k = 12 
    n = len(line)

    n1, idx1 = max((int(line[i]), -i) for i in range(n) if i < n - k + 1)
    k -= 1
    n2, idx2 = max((int(line[i]), -i) for i in range(n) if i > -idx1 and i < n - k + 1)
    k -= 1
    n3, idx3 = max((int(line[i]), -i) for i in range(n) if i > -idx2 and i < n - k + 1)
    k -= 1
    n4, idx4 = max((int(line[i]), -i) for i in range(n) if i > -idx3 and i < n - k + 1)
    k -= 1
    n5, idx5 = max((int(line[i]), -i) for i in range(n) if i > -idx4 and i < n - k + 1)
    k -= 1
    n6, idx6 = max((int(line[i]), -i) for i in range(n) if i > -idx5 and i < n - k + 1)
    k -= 1
    n7, idx7 = max((int(line[i]), -i) for i in range(n) if i > -idx6 and i < n - k + 1)
    k -= 1
    n8, idx8 = max((int(line[i]), -i) for i in range(n) if i > -idx7 and i < n - k + 1)
    k -= 1
    n9, idx9 = max((int(line[i]), -i) for i in range(n) if i > -idx8 and i < n - k + 1)
    k -= 1
    n10, idx10 = max((int(line[i]), -i) for i in range(n) if i > -idx9 and i < n - k + 1)
    k -= 1
    n11, idx11 = max((int(line[i]), -i) for i in range(n) if i > -idx10 and i < n - k + 1)
    k -= 1
    n12, idx12 = max((int(line[i]), -i) for i in range(n) if i > -idx11 and i < n - k + 1)

    max_str = str(n1) + str(n2) + str(n3) + str(n4) + str(n5) + str(n6) + str(n7) + str(n8) + str(n9) + str(n10) + str(n11) + str(n12)
    total += int(max_str)

print(total)
