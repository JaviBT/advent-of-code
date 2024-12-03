import re

raw = open('input.dat').readlines()

pattern = r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))"

matches = re.findall(pattern, ''.join(raw))

result = 0
do = True
for tok in matches:
    if tok == 'do()':
        do = True
        continue
    if tok == 'don\'t()':
        do = False
        continue
    if not do:
        continue
    num1 = tok.split(',')[0].split('(')[1]
    num2 = tok.split(',')[1].split(')')[0]
    result += int(num1) * int(num2)

print(result)