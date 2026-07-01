def move_zeroes(nums):
    insert_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos] = nums[i]
            insert_pos += 1

    for i in range(insert_pos, len(nums)):
        nums[i] = 0


nums = list(map(int, input().split()))
move_zeroes(nums)
print(nums)

move_zeroes(nums)
print(nums)


# 0 1 0 3 12
# [1, 3, 12, 0, 0]