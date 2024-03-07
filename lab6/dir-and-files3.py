import os
 if os.path.exists('/Users/zere/Desktop/check/new.txt'):
   os.remove('/Users/zere/Desktop/check/new.txt')
 else:
   print("The file does not exist")