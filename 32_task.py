import ast
def flat(arr):
    result = []
    for k in arr:
        for elem in k:
            result.append(elem)
    return result


# Для теста - просто присваиваем список напрямую
arr = [(1, 2, 'a'), ('bb', ), ('cc', 'dd', 1)]

result = flat(arr)
print(result)