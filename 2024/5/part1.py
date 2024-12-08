raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

empty_line_index = raw.index('')
raw1 = raw[:empty_line_index]
raw2 = raw[empty_line_index+1:]
raw2 = [[int(x) for x in line.split(',')] for line in raw2]

def check_valid(num, rest):
    for r in rest:
        if int(r) in rule_dict and num in rule_dict[int(r)]:
            return
    return True

rule_dict = {}
for rule in raw1:
    x, y = map(int, rule.split('|'))
    if x not in rule_dict:
        rule_dict[x] = []
    rule_dict[x].append(y)

sum_middle = 0
for order in raw2:
    for i, num in enumerate(order):
        if not check_valid(num, order[i:]):
            break
    else:
        sum_middle += order[len(order)//2]

print(sum_middle)
