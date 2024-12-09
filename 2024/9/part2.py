from tqdm import tqdm

raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]
raw = raw[0]

def calc_free_space(block):
    free_space = {}

    i = 0
    while i < len(block):
        if block[i] == '.':
            start_idx = i
            while i < len(block) and block[i] == '.':
                i += 1
            end_idx = i
            if end_idx - start_idx not in free_space:
                free_space[end_idx - start_idx] = []
            free_space[end_idx - start_idx].append(start_idx)
            free_space[end_idx - start_idx] = sorted(free_space[end_idx - start_idx])
        else:
            i += 1
    
    return free_space

def get_free_fit(wanted_len, free_space):
    min_idx = float('inf')
    for key in free_space.keys():
        if key >= wanted_len and free_space[key][0] < min_idx:
            min_idx = free_space[key][0]
    return min_idx if min_idx != float('inf') else None

if False:
    raw = '2333133121414131402'

cnt = 0
block = []
mem_space = {}
for i, num in enumerate(raw):
    num = int(num)
    if i % 2 == 0:
        mem_space[cnt] = ((len(block), num))
        block += [str(cnt)] * num
        cnt += 1
    else:
        block += ['.' for _ in range(num)]

free_space = calc_free_space(block)

for num, (idx, og_len) in tqdm(sorted(mem_space.items(), key=lambda x: x[0], reverse=True)):
    max_free_space = max(free_space.keys())

    idx_free = get_free_fit(og_len, free_space)
    if idx_free is not None and idx_free < idx:
        block = block[0: idx_free] + block[idx: idx + og_len] + block[idx_free + og_len: idx] + ['.'] * og_len + block[idx + og_len:]
        free_space = calc_free_space(block)

checksum = 0
for i, num in enumerate(block):
    if num == '.':
        continue
    checksum += int(num) * i

print(checksum)
