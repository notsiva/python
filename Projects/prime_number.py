#to identify the prime number 

def is_prime(num):
    if num==0 or num==1:  #to check the given number is 0 or 1, If it is its definitly not a prime number
        print("Not a Prime number")
        
    if num>1: 
        for i in range(2,num): # To loop the number from 2 to the given number
            if num%i==0: # only check if the number is divisible by any other number and the reminder is zero, If its zero then it is not a prime number
                print("Not a Prime number")
                return False
        print("Prime number") #if the if condition doesn't run that means there are no numbers thats divisible and the reminder is zero so the number is prime number


number=int(input("Enter the number for checking Prinme or not: "))
is_prime(num=number)