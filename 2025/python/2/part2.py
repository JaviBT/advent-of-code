raw = open('input.dat').readlines()

def invalid_id(id_number):
    s = str(id_number)
    n = len(s)

    for l in range(1, n):
        if n % l == 0:
            seq = s[:l]
            k = n // l
            kseq = seq * k
            
            if kseq == s:
                return True
                
    return False

ranges = raw[0].split(',')

sm = 0

for inter in ranges:
    start, end = inter.split('-')
    for id in range(int(start), int(end) + 1):
        if invalid_id(int(id)):
            sm += int(id)
            
print(sm)
