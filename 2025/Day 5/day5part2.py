ID_ranges = [tuple(map(int, r.split('-'))) for r in open('day5ranges.txt')]

def merge_ranges(ranges):
    merged = []
    for start, end in sorted(ranges):
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged

merged_ranges = merge_ranges(ID_ranges)
fresh_IDs = sum(end - start + 1 for start, end in merged_ranges)

print(fresh_IDs)