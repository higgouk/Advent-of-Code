with open('day7data') as file:
    data = file.read().splitlines()
    
current_beams = set()
splitters = 0

for line in data:
    if "S" in line:
        current_beams.add(line.index('S'))
    elif "^" in line:
        for ind, char in enumerate(line):
            if char == '^':
                if ind in current_beams:
                    current_beams.remove(ind)
                    current_beams.add(ind-1)
                    current_beams.add(ind+1)
                    splitters += 1

print("splitters", splitters)