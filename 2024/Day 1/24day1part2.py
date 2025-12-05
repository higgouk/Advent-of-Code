data = [tuple(map(int, r.split())) for r in open('24day1data.txt', 'r')]
list_a, list_b = zip(*data)
similarity_total = 0

for num_a in list_a:
    multiplier = 0
    for num_b in list_b:
        if num_a == num_b:
            multiplier += 1
    similarity_score = num_a *multiplier
    similarity_total += similarity_score

print(similarity_total)