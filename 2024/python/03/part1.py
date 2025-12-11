import re

raw = open('input.dat').readlines()

pattern = r"(?:mul\(\d+,\d+\))"

matches = re.findall(pattern, ''.join(raw))

result = 0
for tok in matches:
    num1 = tok.split(',')[0].split('(')[1]
    num2 = tok.split(',')[1].split(')')[0]
    result += int(num1) * int(num2)

print(result)