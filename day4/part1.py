import re

with open("input") as f:
    data = f.read()

result = data.count("XMAS")
result_re = re.findall(r"XMAS", data)
print(result, len(result_re))
