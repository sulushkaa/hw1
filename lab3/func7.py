def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = input("Enter numbers separated by spaces: ")
arr = list(map(int, nums.split()))

result = has_33(arr)


print(result)