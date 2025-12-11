raw = open('input.dat').readlines()

def invalid_id(id):
    s = str(id)
    n = len(s)

    if n % 2 != 0:
        return False

    h = n // 2
    fh = s[:h]
    sh = s[h:]
    
    return fh == sh

ranges = raw[0].split(',')

sm = 0

for inter in ranges:
    start, end = inter.split('-')
    for id in range(int(start), int(end) + 1):
        if invalid_id(int(id)):
            sm += int(id)
            
print(sm)
