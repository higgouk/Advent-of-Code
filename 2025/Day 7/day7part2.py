with open('day7dataTEST') as file:
    data = file.read().splitlines()
    
grid = [list(row) for row in data]

print(grid)
current_beams = set()
total_splitters = 21
timelines = 1
splits = 0

for row_index, row in enumerate(grid):
    if "S" in row:
        current_beams.add(row.index('S'))
    elif "^" in row:
        for char_index, char in enumerate(row):
            if char == '^':
                if char_index in current_beams:
                    current_beams.remove(char_index)
                    current_beams.add(char_index-1)
                    splits += 1
                    break
    elif row_index == len(grid)-1:
        


print("timelines", timelines)
print("splits", splits)