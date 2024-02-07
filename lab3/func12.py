def histogram(numbers):
    for num in numbers:
        print('*' * num)

input_str = input("Enter a list of numbers separated by spaces: ")
nums = [int(num) for num in input_str.split()]

print(histogram(nums))