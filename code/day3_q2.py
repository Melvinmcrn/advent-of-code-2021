file = open("../data/day3.txt", "r")

data = file.read().splitlines()

o2_data = data

index = 0

while len(o2_data) > 1:

  data_0 = []
  data_1 = []

  for current in o2_data:
    if current[index] == '0':
      data_0.append(current)
    elif current[index] == '1':
      data_1.append(current)

  if len(data_1) >= len(data_0):
    o2_data = data_1
  else:
    o2_data = data_0

  index += 1
  if index >= len(data[0]):
    break

co2_data = data

index = 0

while len(co2_data) > 1:

  data_0 = []
  data_1 = []

  for current in co2_data:
    if current[index] == '0':
      data_0.append(current)
    elif current[index] == '1':
      data_1.append(current)

  if len(data_1) >= len(data_0):
    co2_data = data_0
  else:
    co2_data = data_1

  index += 1
  if index >= len(data[0]):
    break

print(o2_data, co2_data, int(o2_data[0], 2) * int(co2_data[0], 2) )