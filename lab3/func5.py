import itertools
def Permutations(word):
    per = itertools.permutations(word)
    for val in per:
      print(*val)

word1  = input("Enter your string:")
Permutations(word1)