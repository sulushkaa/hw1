 import os

 file_path = '/Users/zere/Desktop/check'

 print('Exists:', os.access(file_path, os.F_OK))
 print('Readable:', os.access(file_path, os.R_OK))
 print('Writable:', os.access(file_path, os.W_OK))
 print('Executable:', os.access(file_path, os.X_OK))