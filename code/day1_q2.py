file = open("../data/day1.txt", "r")
lines = file.read().splitlines()

GROUP_AMOUNT = 3

sum_previous_group = 0
sum_current_group = 0

count = 0

for i in range(len(lines)):

  value = int(lines[i])
  if i < GROUP_AMOUNT:
    sum_previous_group += value
  else:
    sum_current_group = sum_previous_group - int(lines[i-GROUP_AMOUNT]) + value

    if sum_previous_group < sum_current_group:
      count += 1

print(count)
