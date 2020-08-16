#Ramirez Gentle Problem 2
number = int(input('Enter a positive number: '))
while number <= 0:
       print('Invalid input.')
       number= int(input("Enter a positive number: "))
#Verification #if negative reprompt
if (number ==1):
   print (a,'is not a prime number')
#Definition. 1 is not a prime number
#else statement runs the for loop
else:  
   count = 0 
   for i in range(2,number):
       if (number%i == 0):
           count = 1
           print(i,'is a divisor of',number,' ...stopping')
           break
#use if and else in for loop and remember identations!
#it stops after the first successful non prime number test
#once you find a number that evenly divides stop testing
       else:
           print(i,'is NOT a divisor of',number,' ...continuing')
   print ()
#print gap
#print statements
   if ( count == 0):
       print(number,'is a prime number!')
#if it goes all the way to the number itself it is prime

   elif ( count == 1):
       print (number,'is not a prime number.')
