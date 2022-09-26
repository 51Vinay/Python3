# this method is use to  the current file position in a string
file1 =open("vinay.txt",'r')
a=file1.seek(5)
print(a)
b=file1.read()
print(b)