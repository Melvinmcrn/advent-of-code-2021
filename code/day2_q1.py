file = open("../data/day2.txt", "r")

horizontal = 0
depth = 0

for line in file:
 
  command, _amount = line.strip().split()
  amount = int(_amount)

  if command == "forward":
    horizontal += amount
  elif command == "down":
    depth += amount
  elif command == "up":
    depth -= amount

    if depth < 0:
      depth = 0

print(horizontal, depth, horizontal*depth)