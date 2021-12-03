file = open("../data/day3.txt", "r")

gamma = 0
epsilon = 0

data = []

for _line in file:
  line = _line.strip()
  if len(data) == 0:
    data = [0 for _ in range(len(line))]

  for i in range(len(line)):
    current_digit = line[i]

    if current_digit == '0':
      data[i] -= 1
    elif current_digit == '1':
      data[i] += 1

total_digit = len(data)
for i in range(total_digit):
  if (data[i] < 0):
    epsilon += 2**(total_digit-i-1)
  else:
    gamma += 2**(total_digit-i-1)

print(gamma, epsilon, gamma*epsilon)