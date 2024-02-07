def solve(numheads, numlegs):
    chickens = int
    rabbits = int
    rabbits =  numlegs/2 - numheads 
    chickens = numlegs/2 - rabbits*2 
    return (chickens), (rabbits)

numheads_input = int(input("Enter the number of heads: "))
numlegs_input = int(input("Enter the number of legs: "))

result = solve(numheads_input, numlegs_input)
print("Number of chickens:", result[0])
print("Number of rabbits:", result[1])