import math

with open('day6data') as file:
    grid = file.read().splitlines()

total_rows = len(grid)
total_columns = max(len(row) for row in grid)
current_column = 0
total_equations  = 0
equation = []
nums = []
operation = []

while current_column <= total_columns:
    for row_index, row in enumerate(grid):
        char = row[current_column] if current_column < len(row) else " "
        if row_index < total_rows - 1:
            nums.append(char)
        elif row_index == total_rows - 1:
            operation.append(char)
    if all(ch == " " for ch in nums):
        if operation[0] == '*':
            equation_result = math.prod(equation)
            total_equations += equation_result
        elif operation[0] == '+':
            equation_result = sum(equation)
            total_equations += equation_result
        current_column += 1
        equation = []
        operation = []
        continue
    joined = ''.join(nums).strip()
    nums = []
    equation.append(int(joined))
    current_column += 1

print(total_equations)