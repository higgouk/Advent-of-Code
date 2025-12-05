data = [tuple(map(int, r.split())) for r in open('24day1data.txt', 'r')]
list_a, list_b = zip(*data)
total_difference = 0

zipped_sorted = list(zip(sorted(list_a), sorted(list_b)))
for pair in zipped_sorted:
    left, right = pair
    difference = abs(right - left)
    total_difference += difference

print(total_difference)