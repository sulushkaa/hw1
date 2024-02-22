def divisible_by_3_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i%4 == 0 :
           yield i 
a = int(input("Enter a number:"))
nums = divisible_by_3_4(a)
for num in nums:
    print(num) 