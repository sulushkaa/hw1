def Farenheit_to_centigrade(F):
    C = (5/9) * (F-32)
    return C

farenheit = float(input("Enter temperature in Farenheits:"))
result = Farenheit_to_centigrade(farenheit)
print(result)