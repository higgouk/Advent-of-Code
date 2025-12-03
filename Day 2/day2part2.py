with open('day2data', 'r') as data:
    product_ranges = data.read().strip().split(",")

total = 0

def equal_parts(s, n):
    part_length = len(s) // n
    parts = [s[i:i + part_length] for i in range(0, len(s), part_length)]
    if len(set(parts)) == 1:
        return True
    return None


for product_range in product_ranges:
    (start, end) = product_range.split("-")
    for product in range(int(start), int(end) + 1):
        string = str(product)
        for length in range(len(string) + 1):
            if equal_parts(string, len(string)):
                total += product

print(total)
