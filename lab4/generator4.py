def square_numbers(a,b):
    for i in range(a, b):
        yield(i*i)

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
mynums = square_numbers(first, second)
for num in mynums:
    print(num)