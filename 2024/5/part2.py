from collections import defaultdict, deque

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

raw3 = []
for order in raw2:
    for i, num in enumerate(order):
        if not check_valid(num, order[i:]):
            raw3.append(order)
            break

# Fix orders in raw3
def fix_order(order, rule_dict):
    # Create a graph representation
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Add edges based on rules in rule_dict
    for x in order:
        if x in rule_dict:
            for y in rule_dict[x]:
                if y in order:  # Only consider dependencies within this order
                    graph[x].append(y)
                    in_degree[y] += 1

    # Initialize in-degree for all nodes in the order
    for x in order:
        if x not in in_degree:
            in_degree[x] = 0

    # Topological sorting using Kahn's algorithm
    queue = deque([x for x in order if in_degree[x] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we have a valid topological sort, return it
    if len(sorted_order) == len(order):
        return sorted_order
    else:
        raise ValueError("Cannot resolve dependencies for order:", order)

fixed_raw3 = []
for order in raw3:
    fixed_raw3.append(fix_order(order, rule_dict))

sum_middle = 0
for order in fixed_raw3:
    for i, num in enumerate(order):
        if not check_valid(num, order[i:]):
            break
    else:
        sum_middle += order[len(order)//2]

print(sum_middle)
