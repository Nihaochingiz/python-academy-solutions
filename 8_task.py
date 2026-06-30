# s = input()
# width = int(input())

s = 'ABCDEFGHIJKLIMNОQRSTUVWXYZ'
width = 4

result = ''

for i in range(0, len(s), width):
    result += s[i:i+width] + '\n'

print(result)