raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]
raw = raw[0]

if False:
    raw = '2333133121414131402'

cnt = 0
block = []
for i, num in enumerate(raw):
    num = int(num)
    if i % 2 == 0:
        block += [str(cnt)] * num
        cnt += 1
    else:
        block += ['.' for _ in range(num)]

i = 0
checksum = 0
while i < len(block):
    while block[i] == '.':
        block[i] = block.pop()
    checksum += int(block[i]) * i
    i += 1

print(checksum)
