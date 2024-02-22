    def numbers(n):
    for i in range(n):
        if i%2 == 0:
            yield i
a = int(input("Enter a number:"))
my_list = numbers(a)
mystring =" ".join(map(str, my_list))
print(mystring )