def find_missing_number(numbers):
    if len(numbers) == 1:
        return numbers[0] + 1
    i = 1
    nums = sorted(numbers)
    while i < len(nums):
        if nums[i] - 1 != nums[i -1]:
            return nums[i] -1
        i += 1
    return nums[-1] + 1
print(find_missing_number([2, 3, 1, 5]))