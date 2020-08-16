#Part 2b: Find all Prime Numbers between 1 and 1000

for number in range(1,1001):
#range is not inclusive of 100, has to be the number plus 1
   if (number ==1):
       print (number,'is technically not a prime number.')
#while/foor loop will keep going after 1
   else:  
       x = 0
       for i in range(2,number):
           #number is the variable here not 1001 becuase in the for\\
           #loop it will subsitute each number
           if (number%i == 0):
               x = 1
               break
            #similar to 2A if x ==1 it is not a prime number
            #no need to print this just skip to the next. 

       if ( x == 0):
           print(number,'is a prime number!')

