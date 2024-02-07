def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

# Example usage1
numbers_str = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers_str.split()]

prime_numbers = filter_prime(numbers_list)

print("Original list:", numbers_list)
print("Prime numbers:", prime_numbers)