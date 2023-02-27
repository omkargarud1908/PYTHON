"1) Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’." 

n = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (1, n + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  