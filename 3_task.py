# https://python-academy.org/ru/trainer/tasks/3

n = int(input())
scores = list(map(int, input().split()))

def get_second_max_sorted(nums):
    unique_nums = sorted(list(set(nums))) # Удаляем дубликаты
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2] # Берем второй элемент с конца

print(get_second_max_sorted(scores))  # Выведет: 5
