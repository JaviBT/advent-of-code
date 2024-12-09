raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

def is_valid(current_result, values, test_result):
    if (current_result == test_result and not values):
        return True
    if current_result > test_result or (current_result != test_result and not values):
        return False
    
    return is_valid(current_result + values[0], values[1:], test_result) or is_valid(current_result * values[0], values[1:], test_result)

sum = 0
for line in raw:
    test_result = int(line.split(': ')[0])
    values = [int(x) for x in line.split(': ')[1].split(' ')]
    if is_valid(0, values, test_result):
        sum += test_result

print(sum)
