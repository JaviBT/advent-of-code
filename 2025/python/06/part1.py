import math
raw = open('input.dat').readlines()

numbers = []
operators = []

lines = raw

for line in lines[:-1]:
    numbers.append([int(x) for x in line.split()])

operators = lines[-1].split()

total = 0
for i in range(len(numbers[0])):
  if operators[i] == '*':
    curSum = 1
    for j in range(len(numbers)):
      curSum *= numbers[j][i]
  elif operators[i] == '+':
    curSum = 0
    for j in range(len(numbers)):
      curSum += numbers[j][i]
  total += curSum

print(total)
