#readable method is use to check available file mode is readable or not
a=open('vinay.txt',encoding='utf-8',mode='r',buffering=1)
b=a.readable()
print(b)