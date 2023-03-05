str=input("enter string:")
l1=[]
for i in str:
    if(i>='A' and i<='Z' or i>='a' and i<='z'):
        l1+=i
print(l1)