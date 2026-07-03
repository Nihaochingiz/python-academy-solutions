def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) / 2
    actual_sum = sum(nums)
    return int((expected_sum - actual_sum))

# Чтение входных данных
nums = list(map(int, input().split()))
result = missing_number(nums)
print(result)