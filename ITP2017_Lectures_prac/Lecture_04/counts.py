import pprint
data_list = [0, 1, 1, 3, 1, 3, 6, 1, 8, 2, 8, 7, 5, 0, 2, 2, 1, 5, 4, 7, 0, 0, 3, 1, 2, 9, 9, 4, 3, 2, 5, 3, 1, 2, 1, 3,
             3, 2, 2, 4, 5, 1, 6, 7, 9, 8, 1, 4, 2, 5, 6, 8, 0, 0, 0, 1, 1, 2, 6, 1, 3, 2, 4, 2, 5, 7, 3, 1, 3, 4, 6]

counts = {}
print(counts)

for num in data_list:
    if num in counts:
        counts[num] = counts[num] + 1
    else:
        counts[num] = 1

pprint.pprint(counts)
