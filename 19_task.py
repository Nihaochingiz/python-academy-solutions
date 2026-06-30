def fizzbuzz(n):
    fblist = []
    for digit in range(1, n + 1):
        if digit % 3 == 0 and digit % 5 == 0:
            fblist.append('FizzBuzz')
        elif digit % 3 == 0:
            fblist.append('Fizz')
        elif digit % 5 == 0:
            fblist.append('Buzz')
        else:
            fblist.append(str(digit))
    return fblist


n = int(input().strip())
result = fizzbuzz(n)

for item in result:
    print(item)