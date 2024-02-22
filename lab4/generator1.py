def squares(n):
 for i in range(n):
  yield (i*i)
a = int(input("Enter a  number:"))
mynums = squares(a)
print (mynums)
for num in mynums:
 print(num)