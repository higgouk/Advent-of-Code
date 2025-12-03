with open('day2dataTEST', 'r') as data:
    product_ranges = data.read().strip().split(",")

total = 0

def equal_parts(string, part_length):
    parts = [string[i:i + part_length] for i in range(0, len(string), part_length)]
    print(parts)
    if len(set(parts)) == 1:
        return True
    return None

for product_range in product_ranges:
    (start, end) = product_range.split("-")
    for product in range(int(start), int(end) + 1):
        product_string = str(product)
        length = len(product_string)
        for n in range(1, length // 2):
            if equal_parts(product_string, n):
                total += product

print(total)