data1 = open('day5ranges.txt', 'r')
data2 = open('day5IDs.txt', 'r')
ID_ranges = data1.read().strip().splitlines()
IDs = data2.read().strip().splitlines()
fresh = set()

for ID_range in ID_ranges:
    start, end = ID_range.split('-')
    for ID in IDs:
        if int(start) <= int(ID) <= int(end):
            fresh.add(ID)

print("fresh:", len(fresh))