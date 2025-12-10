import re
from collections import deque

def apply_button(state, button):
    new_state = list(state)
    for i in range(len(state)):
        if button[i] == 1:
            if new_state[i] == 1:
                new_state[i] = 0
            else:
                new_state[i] = 1
    return new_state

raw = open('input.dat').readlines()

total_presses = 0

for line in raw:
    line = line.strip()

    # Parse line
    match = re.match(r'^\[([.#]+)\]\s+(.*)\s+\{(.*)\}$', line)
    diagram_str = match.group(1)
    buttons_str = match.group(2)

    # Parse to integer list
    diagram = [1 if x == '#' else 0 for x in diagram_str]
    
    # Parse buttons into bitmask lists
    buttons = []
    for i, b_str in enumerate(buttons_str.split(' ')):
        newB = b_str.strip('()').split(',')
        bitB = []
        for j in range(len(diagram)):
            if str(j) in newB:
                bitB.append(1)
            else:
                bitB.append(0)
        buttons.append(bitB)

    # BFS
    queue = deque([(diagram, 0)])
    visited = {tuple(diagram)}
    
    found_presses = 0
    
    found = False
    while queue:
        current_state, dist = queue.popleft()
        
        if all(x == 0 for x in current_state):
            found_presses = dist
            found = True
            break
        
        for btn in buttons:
            next_state = apply_button(current_state, btn)
            
            state_tuple = tuple(next_state)
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((next_state, dist + 1))

    total_presses += found_presses

print(total_presses)
