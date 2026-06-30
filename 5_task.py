from itertools import groupby

s = input().strip()

runs = [(sum(1 for _ in g), int(k)) for k,g in groupby(s)]

strings = []

for count,digit in runs:
    strings.append(f"({count}, {digit})")
result = " ".join(strings)
print(result)