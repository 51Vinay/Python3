#Writelines- this method is use to write in existiong file
#'a' - append mode is use to write in file without overwriting
f=open('vinay.txt','a')
e=f.writelines(['python is a dynamic typed programming language /n python is a open souce programming language'])
print(e)