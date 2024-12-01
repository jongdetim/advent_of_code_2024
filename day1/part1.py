#parse, sort, subtract, absolute, add to total

with open("input") as file:
    data = [(int(num[0]), int(num[1])) for num in (line.split() for line in file)]

# rotate data 90 degrees
data = [list(i) for i in zip(*data)][::-1]

# sort data
sorted_data = []
for i, row in enumerate(data):
    sorted_data.append(sorted(row))

total = 0
for rownum in range(len(sorted_data[0])):
    total += abs(sorted_data[0][rownum] - sorted_data[1][rownum])
    # print(total)

print(total)
