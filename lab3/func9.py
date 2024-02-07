def has_007(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i+2]==7 :
            return True
    return False

nums = input("Enter numbers separated by spaces: ")
arr = list(map(int, nums.split()))

result = has_007(arr)


print(result)
