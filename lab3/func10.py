def unique_elements(first):
    unique_list = []
    for element in first:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_str.split()]

result_list = unique_elements(numbers)

print("Unique elements:", result_list)