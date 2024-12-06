
# f2=open(r"D:\python_programs\ch1\print_escape_seq.py")   # Opening file from different folders
# print(f2.read())
# f2.close()

f1=open('text.text')     # Opening file in same folder

print(f1.tell())         # Location of cursor
print(f1.readline())     # Read one line only
print(f1.readlines())    # Creates list of lines
f1.seek(0)               # Moving cursor
print('\n',f1.read())    # Reading whole file
print(f1.tell())         # Location of cursor

f1.close()               # Closing file
