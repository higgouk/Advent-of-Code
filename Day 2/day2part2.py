with open('day2data', 'r') as data:
    product_ranges = data.read().strip().split(",")

total = 0

def equal_parts(s, n):
    part_length = len(s) // n
    parts = [s[i:i + part_length] for i in range(0, len(s), part_length)]
    # print(parts)
    if len(set(parts)) == 1:
        return True
    return None

for product_range in product_ranges:
    (start, end) = product_range.split("-")
    for product in range(int(start), int(end) + 1):
        string = str(product)
        length = len(string)
        for l in range(2, length):
            if equal_parts(string, l):
                total += product

print(total)
