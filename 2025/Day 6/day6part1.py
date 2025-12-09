import math

with open('day6data') as file:
    grid = [line.split() for line in file]

total_rows = len(grid)
total_columns = len(grid[0])
total_equations  = 0
current_column = 0

while current_column < total_columns:
    equation = []
    for row_index, row in enumerate(grid):
        if row_index < total_rows - 1:
            equation.append(int(row[current_column]))
        elif row[current_column] == '*':
            equation_result = math.prod(equation)
            total_equations += equation_result
        elif row[current_column] == '+':
            equation_result = sum(equation)
            total_equations += equation_result
    current_column += 1

print(total_equations)