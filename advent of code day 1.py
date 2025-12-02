with open('data.txt', 'r') as data:
    instructions = data.read().strip().splitlines()

current_number = 50
zero_count = 0
wheel_size = 100

for line in instructions:
    direction = line[0]
    distance = int(line[1:])
   # print(f"direction: ", direction, "distance: ", distance)

    if direction == "R":
        zero_count += (current_number + distance) // wheel_size
        current_number = (current_number + distance) % wheel_size
       # print(f"zeros: ", zero_count, "current number: ", current_number)
    else:
        zero_count += (distance - 1 + (wheel_size - current_number)) // wheel_size
        current_number = (current_number - distance) % wheel_size
    # print(f"direction: ", direction, "distance: ", distance)

print(zero_count)