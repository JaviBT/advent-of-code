import re
import sys
from collections import deque
from z3 import *

def parse_line(line):
    line = line.strip()

    # Parse line
    match = re.match(r'^\[([.#]+)\]\s+(.*)\s+\{(.*)\}$', line)
    buttons_str = match.group(2)
    joltages_str = match.group(3)

    # Parse joltages
    joltages = [int(x) for x in joltages_str.split(',')]

    # Parse buttons into bitmask lists
    buttons = []
    for i, b_str in enumerate(buttons_str.split(' ')):
        newB = b_str.strip('()').split(',')
        bitB = []
        for j in range(len(joltages)):
            if str(j) in newB:
                bitB.append(1)
            else:
                bitB.append(0)
        buttons.append(bitB)
    
    return joltages, buttons

def solve_bfs(joltages, buttons):
    queue = deque([(tuple(joltages), 0)])
    visited = {tuple(joltages)}
    
    while queue:
        curr, steps = queue.popleft()
        
        if all(x == 0 for x in curr):
            return steps
        
        for btn in buttons:
            next_state = []
            valid = True
            for c, b in zip(curr, btn):
                rem = c - b
                if rem < 0:
                    valid = False
                    break
                next_state.append(rem)
            
            if valid:
                next_state = tuple(next_state)
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))
    
    return None

def solve_z3(joltages, buttons):
    s = Optimize()
    
    # Variables: number of times each button is pressed
    x = [Int(f'x_{i}') for i in range(len(buttons))]
    
    # Constraints: x_i >= 0
    for var in x:
        s.add(var >= 0)
        
    # Constraints: A * x = target
    for r in range(len(joltages)):
        expr = Sum([x[c] for c in range(len(buttons)) if buttons[c][r] == 1])
        s.add(expr == joltages[r])
        
    # Objective: Minimize sum(x)
    total_presses_var = Sum(x)
    s.minimize(total_presses_var)
    
    check_result = s.check()
    if check_result == sat:
        m = s.model()
        presses = m.eval(total_presses_var).as_long()
        return presses

raw = open('input.dat').readlines()

total_presses = 0

# Toggle this to switch methods
# Note: BFS is much slower than Z3 and unfeasible for the full input
USE_Z3 = True 

for line in raw:
    joltages, buttons = parse_line(line)
    
    if USE_Z3:
        res = solve_z3(joltages, buttons)
    else:
        res = solve_bfs(joltages, buttons)
    
    total_presses += res

print(total_presses)
