with open('day2data', 'r') as data:
    product_ranges = data.read().strip().split(",")

total = 0

for product_range in product_ranges:
    (start, end) = product_range.split("-")
    for product in range(int(start), int(end) + 1):
        string = str(product)
        middle = len(string) // 2
        first_half = string[:middle]
        second_half = string[middle:]
        if first_half == second_half:
            total += product

print(total)