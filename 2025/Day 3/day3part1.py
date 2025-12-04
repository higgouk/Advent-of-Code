with open('day3data', 'r') as data:
    banks = data.read().strip().splitlines()

total_joltage = 0

for bank in banks:
    joltage_list = []
    bank_list = list(bank)
    max_index = bank_list.index(max(bank_list))
    joltage_list.append(bank_list[max_index])
    if max_index != len(bank_list) - 1:
        bank_list = bank_list[max_index+1:]
        max_index = bank_list.index(max(bank_list))
        joltage_list.append(bank_list[max_index])
    else:
        bank_list.pop()
        max_index = bank_list.index(max(bank_list))
        joltage_list.insert(0, bank_list[max_index])
    joltage_int = [int(num) for num in joltage_list]
    combined = int("".join(str(n) for n in joltage_int))
    total_joltage += combined

print(total_joltage)