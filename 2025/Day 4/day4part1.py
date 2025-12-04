with open('day4data', 'r') as data:
    rows = data.read().strip().splitlines()

grid = [list(row) for row in rows]
rows_number = len(grid)
columns_number = len(grid[0])

roll_total = 0

def get_neighbours(row, column):
    count = 0
    for delta_row in (-1, 0, 1):
        for delta_column in (-1, 0, 1):
            if delta_row == 0 and delta_column == 0:
                continue
            new_row = row + delta_row
            new_column = column + delta_column
            if 0 <= new_row < rows_number and 0 <= new_column < columns_number:
                if grid[new_row][new_column] == '@':
                    count += 1
    return count

for r in range(rows_number):
    for c in range(columns_number):
        if grid[r][c] == '.':
            continue
        if get_neighbours(r, c) < 4:
            roll_total += 1

print(roll_total)