def file_lengthy(namik):
         with open(namik) as f:
                 for i, l in enumerate(f):
                         pass
         return i + 1
 print("Number of lines in the file: ",file_lengthy('/Users/zere/Desktop/check/new.txt'))