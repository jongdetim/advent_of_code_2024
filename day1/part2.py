#parse, count row 2 for every occurence in row 1, add to total

with open("input") as file:
    data = [(int(num[0]), int(num[1])) for num in (line.split() for line in file)]

# rotate data 90 degrees
data = [list(i) for i in zip(*data)][::-1]

total = 0
for rownum in range(len(data[0])):
    total += data[1].count(data[0][rownum]) * data[0][rownum]

print(total)
