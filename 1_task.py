# https://python-academy.org/ru/trainer/tasks/1

numbers = list(map(int, input().split()))

def mul(list_):
    n = 1
    for el in list_:
        n *= el
    return n

print(mul(numbers))