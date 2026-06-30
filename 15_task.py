def find_median(input_string):
    numbers = [int(x) for x in input_string.split()]
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)

    if n % 2 == 0:
        sum_middle = sorted_nums[n // 2 - 1] + sorted_nums[n // 2]

        if sum_middle % 2 == 0:
            return str(sum_middle // 2)

        else:
            return f"{sum_middle / 2:.1f}"
    else:
        return str(sorted_nums[n // 2])


input_string = input().strip()
result = find_median(input_string)
print(result)