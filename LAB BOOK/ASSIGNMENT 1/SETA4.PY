"""4) Write a program which finds sum of digits of a number.
Example n=130 then output is 4 (1+3+0)."""

n=int(input("enter a number:"))
sum=0
while(n>0):
    num = n % 10
    sum=sum + num
    n=n//10
print(sum)
