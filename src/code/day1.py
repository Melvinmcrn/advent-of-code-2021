file = open("../data/day1.txt", "r")

previous_value = None
larger_count = 0

for line in file:
  value = int(line.strip())

  if previous_value is not None and  value > previous_value:
    larger_count += 1
    
  previous_value = value

file.close()

print("Count larger:", larger_count)