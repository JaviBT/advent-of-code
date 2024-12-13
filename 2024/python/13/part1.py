import re
import math
from tqdm import tqdm

raw = open('input.dat').readlines()
raw = [line.strip() for line in raw]

if False:
    raw = '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''.strip().split('\n')


machines = []
for input in raw:
    if input == '': continue
    match_button = re.match(r'Button [AB]: X\+(-?\d+), Y\+(-?\d+)', input)
    match_prize = re.match(r'Prize: X=(\d+), Y=(\d+)', input)


    # Check start character 'Button A: ' (Ecample: 'Button A: X+21, Y+40', 'Button B: X+56, Y+21', 'Prize: X=15390, Y=2402')
    if input.startswith('Button A:'):
        parts = input.split(':')
        dx_a, dy_a = map(int, match_button.groups())
    elif input.startswith('Button B:'):
        parts = input.split(':')
        dx_b, dy_b = map(int, match_button.groups())
    elif input.startswith('Prize:'):
        parts = input.split(':')
        px, py = map(int, match_prize.groups())
        machines.append({'A': (dx_a, dy_a), 'B': (dx_b, dy_b), 'prize': (px, py)})

def min_tokens_grid(machine):
    dx_a, dy_a = machine['A']
    dx_b, dy_b = machine['B']
    px, py = machine['prize']
    cost_a, cost_b = 3, 1

    # Create DP table with size px, py
    dp = [[math.inf] * (py + 1) for _ in range(px + 1)]
    dp[px][py] = 0

    # Reverse traverse the DP table updating the positions accordingly
    for x in range(px, -1, -1):
        for y in range(py, -1, -1):
            if dp[x][y] == math.inf: continue

            # Press A:
            dp[x - dx_a][y - dy_a] = min(dp[x - dx_a][y - dy_a], dp[x][y] + cost_a)

            # Press B:
            dp[x - dx_b][y - dy_b] = min(dp[x - dx_b][y - dy_b], dp[x][y] + cost_b)

    return dp[0][0]

def min_tokens_dict(machine, max_button_presses=200):
    dx_a, dy_a = machine['A']
    dx_b, dy_b = machine['B']
    px, py = machine['prize']
    cost_a, cost_b = 3, 1

    dp = {(0, 0): 0} 

    for _ in range(max_button_presses):
        new_dp = dict(dp) 
        for (x, y), cost in dp.items():
            # Press A
            new_x, new_y = x + dx_a, y + dy_a
            new_cost = cost + cost_a
            if (new_x <= px and new_y <= py) and ((new_x, new_y) not in new_dp or new_dp[(new_x, new_y)] > new_cost):
                new_dp[(new_x, new_y)] = new_cost
            
            # Press B
            new_x, new_y = x + dx_b, y + dy_b
            new_cost = cost + cost_b
            if (new_x <= px and new_y <= py) and ((new_x, new_y) not in new_dp or new_dp[(new_x, new_y)] > new_cost):
                new_dp[(new_x, new_y)] = new_cost
        
        dp = new_dp

        if (px, py) in new_dp:
            break

    # Return the cost to reach the prize position if reachable
    return dp.get((px, py), math.inf)


total_tokens = 0
for machine in tqdm(machines):
    new_tokens = min_tokens_dict(machine)
    total_tokens += new_tokens if new_tokens != math.inf else 0

print(total_tokens)
