"4) Write a program to reverse a given number."

n=int(input("enter a number:"))
s=[]
while(n>0):
    num = n % 10
    n=n//10
    s.append(num)
    print(num)
print(s)