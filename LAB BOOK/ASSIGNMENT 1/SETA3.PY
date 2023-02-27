"""3) Write a program which accepts an integer value as command line and print “Ok” if value is 
between 1 to 50 (both inclusive) otherwise it prints” Out of range”. """


import sys
n=sys.argv[1]
if n < 50 :
    print("ok")
else:
    print("Out of range")
