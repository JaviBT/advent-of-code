import sys

sys.setrecursionlimit(5000)

raw = open('input.dat').readlines()

devices = {}
for line in raw:
    device, outputs = line.strip().split(':')
    devices[device.strip()] = [str(x) for x in outputs.strip().split(' ') if x != '']

memo = {}

def traverse(device, dac, fft):
    state = (device, dac, fft)
    if state in memo:
        return memo[state]
    
    if device == 'dac': dac = True
    if device == 'fft': fft = True
    
    if device == 'out':
        return 1 if dac and fft else 0
        
    num_paths = 0
    for output in devices[device]:
        num_paths += traverse(output, dac, fft)
    memo[state] = num_paths
    return num_paths

print(traverse('svr', False, False))
