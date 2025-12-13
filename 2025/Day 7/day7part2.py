from collections import defaultdict

with open('day7data') as file:
    lines = file.read().splitlines()

beams = defaultdict(int)
splitters = 0

start_col = lines[0].index('S')
beams[start_col] = 1

for line in lines[::2]:
    for col in tuple(beams.keys()):
        if line[col] == '^':
            splitters += 1
            count = beams[col]
            beams[col - 1] += count
            beams[col + 1] += count
            del beams[col]

print("splitters", splitters)
print("timelines", sum(beams.values()))