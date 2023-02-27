"1) Write a Python Program to Calculate the Average of Numbers in a Given List."

n=int(input("enter number:"))
sum=0
l1=[]
for i in range(n):
    print("enter elements:",i+1)
    x=int(input())
    l1.append(x)
sum=sum+l1[i]
avg=sum/n
print("average is :",avg)