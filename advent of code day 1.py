with open('data.txt', 'r') as data:
    instructions = data.read().strip().splitlines()
current_number = 50
zero_count = 0

for line in instructions:
    direction = line[0]
    value = int(line[1:])
    if direction == "R":
        current_number = (current_number + value) % 100
    else:
        current_number = (current_number - value) % 100
    if current_number == 0:
        zero_count += 1

print(zero_count)