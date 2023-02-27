"""2) Write a program which accepts 6 integer values and prints “DUPLICATES” if any of the 
values entered are duplicates otherwise it prints “ALL UNIQUE”.
 Example: Let 5 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed."""

n=6
s=[]
s2=[]
for i in range (n):
    print("enter number",i+1)
    x=int(input())
    s.append(x)
print(s)
for i in s:
    if i not in s2:
            s2.append(i)
print(s2)

if len(s)==len(s2):
     print("ALL UNIQUE")
else:
     print("DUPLICATES")
