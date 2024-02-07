def convert_units (grams):
    ounces = 28.3495231 * grams
    return ounces

grams_needed = float(input("Enter the amount in grams:"))
result = convert_units(grams_needed)
print (result)