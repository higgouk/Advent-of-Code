with open('day3data', 'r') as data:
    banks = data.read().strip().splitlines()

total_joltage = 0
result_length = 12

for bank in banks:
    step = result_length
    joltage_list = []
    bank_list = [int(num) for num in bank]
    while step > 0:
        bank_subset = bank_list[:len(bank_list) - step + 1]
        max_index = bank_subset.index(max(bank_subset))
        joltage_list.append(bank_subset[max_index])
        bank_list = bank_list[max_index + 1:]
        step -= 1
    combined = int("".join(str(num) for num in joltage_list))
    total_joltage += combined

print(total_joltage)