import numpy as np

with open('day8data') as file:
    data = file.read().splitlines()

pairs = []

for index, line1 in enumerate(data):
    x, y, z = map(int, line1.split(','))
    point_1 = np.array([x, y, z])
    for line2 in data[index+1:]:
        x2, y2, z2 = map(int, line2.split(','))
        point_2 = np.array([x2, y2, z2])
        if point_2[0] != point_1[0]:
            dist = float(np.sqrt(np.sum((point_1-point_2) ** 2)))
            tuple = (line1, line2, dist)
            pairs.append(tuple)
    
sorted_pairs = sorted(pairs, key=lambda t: t[2])
thousand_shortest = sorted_pairs[0:1000]
circuits = []

while len(thousand_shortest) > 0:
    circuit = []
    circuit.append(thousand_shortest[0][:2])
    thousand_shortest.pop(0)

    for c in circuit:
        for p1, p2, d in thousand_shortest:
            if p1 in c and p2 in c:
                thousand_shortest.remove((p1, p2, d))
            elif p1 in c or p2 in c:
                circuit.append((p1, p2))
                thousand_shortest.remove((p1, p2, d))
    circuits.append(circuit)

circuit_lengths = []
for c in circuits:
    junctions = {point for p1, p2 in c for point in (p1, p2)}
    circuit_lengths.append(len(junctions))

circuit_lengths.sort(reverse=True)
ans = circuit_lengths[0] * circuit_lengths[1] * circuit_lengths[2]
print(ans)
