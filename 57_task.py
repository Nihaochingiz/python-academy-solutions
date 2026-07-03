def add_binary(a, b):
    sum_dec = int(a, 2) + int(b, 2)
    return bin(sum_dec)[2:]

# Чтение входных данных
a = input().strip()
b = input().strip()
result = add_binary(a, b)
print(result)