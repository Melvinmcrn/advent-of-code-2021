file = open("../data/day2.txt", "r")

horizontal = 0
depth = 0
aim = 0

for line in file:
 
  command, _amount = line.strip().split()
  amount = int(_amount)

  if command == "forward":
    horizontal += amount
    depth += aim*amount
  elif command == "down":
    aim += amount
  elif command == "up":
    aim -= amount


print(horizontal, depth, horizontal*depth)