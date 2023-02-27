"""2) Write a program that accept two integer values and if both are equal then prints “SAME 
identity” otherwise prints, “DIFFERENT identity”."""

X=int(input("enter x integer:"))
Y=int(input("enter x integer:"))
ans=X is Y
print(ans)

if ans==True:
    print("same identity")
else:
    print("Different identity")