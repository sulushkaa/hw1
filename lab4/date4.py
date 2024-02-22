from datetime import datetime

x_str = input("Enter first date:")
y_str = input("Enter second date:")
x = datetime.strptime(x_str, "%Y-%m-%d %H:%M:%S")
y = datetime.strptime(y_str, "%Y-%m-%d %H:%M:%S")
a = x - y
print(a.total_seconds())