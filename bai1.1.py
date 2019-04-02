n=input("Nhap chuoi:")
dict ={'H:0','T':0}
for i in n:
    if i.isupper():
        dict['H']=dict['H']+1
    elif i!=' ':
        dict ['T']+=1
print(dict)