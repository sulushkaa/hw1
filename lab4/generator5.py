def numbers(n):
    while n>=0 :
      yield n
      n -= 1
n = int(input("Enter your number:"))

for num in numbers(n):
   print(num)