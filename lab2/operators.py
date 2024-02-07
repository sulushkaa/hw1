#ex1
x = 5
y = 10
print(x+y)

#ex2
print(x-y)

#ex3
print(x*y)

#ex4
print(x/y)

#ex5
print(x%y)

#ex6
print(x**y)

#ex7
x = 15
y = 2
print(x//y)

#ex8
x += 3
print(x)

#ex9
x -=3
print(x)

#ex10
x *= 3
print(x)

#ex11
x /= 3
print(x)

#ex12
x %= 2
print(x)

#ex13
x = 5

x//=3

print(x)

#ex14
x = 5

x **= 3

print(x)

#ex15
x = 5

x &= 3

print(x)

#ex16
x = 5

x |= 3

print(x)

#ex17
x = 5

x ^= 3

print(x)

#ex18
x = 5

x >>= 3

print(x)

#ex19
x = 5

x <<= 3

print(x)

#ex20
x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3

#ex21
x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3

#ex22
x = 5
y = 3

print(x > y)

# returns True because 5 is greater than 3

#ex23
x = 5
y = 3

print(x < y)

# returns False because 5 is not less than 3

#ex24
x = 5
y = 3

print(x >= y)

# returns True because five is greater, or equal, to 3

#ex25
x = 5
y = 3

print(x <= y)

# returns False because 5 is neither less than or equal to 3

#ex26
x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10

#ex27
x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)

#ex28
x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result

#ex29
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#ex30

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#ex31
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#ex32
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

#ex33
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

print((6 + 3) - (6 + 3))

print(100 + 5 * 3)
