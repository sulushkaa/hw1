 import os

 path = r'/Users/zere/Desktop/check/new.txt'
 print(os.path.exists(path))
 print("\nFile name of the path:")
 print(os.path.basename(path))
 print("\nDir name of the path:")
 print(os.path.dirname(path))