
raw = open('input.dat').readlines()

devices = {}
for line in raw:
    device, outputs = line.strip().split(':')
    devices[device.strip()] = [str(x) for x in outputs.strip().split(' ') if x != '']

def traverse(device, visited):
    if device == 'out':
        return 1

    num_paths = 0
    for output in devices[device]:
        if output not in visited:
            num_paths += traverse(output, visited + [output])
    return num_paths

print(traverse('you', ['you']))
