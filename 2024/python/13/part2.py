import re
import math
import numpy as np
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
        machines.append({'A': (dx_a, dy_a), 'B': (dx_b, dy_b), 'prize': (px + 10000000000000, py + 10000000000000)})

def min_tokens_numpy(machine):
    dx_a, dy_a = machine['A']
    dx_b, dy_b = machine['B']
    px, py = machine['prize']
    cost_a, cost_b = 3, 1

    A = np.array([[dx_a, dy_a], [dx_b, dy_b]]).T
    b = np.array([px, py])

    solution = np.linalg.solve(A, b)

    a, b = solution
    a, b = round(a), round(b)

    if a * dx_a + b * dx_b == px and a * dy_a + b * dy_b == py:
        return a * cost_a + b * cost_b

    return math.inf

total_tokens = 0
for machine in tqdm(machines):
    new_tokens = min_tokens_numpy(machine)
    total_tokens += new_tokens if new_tokens != math.inf else 0

print(total_tokens)
