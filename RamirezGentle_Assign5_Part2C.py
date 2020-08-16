#Ramirez Gentle Assignment 5 Part 2C

while True:
   start = int(input('Start number: '))
   end = int(input('End number: '))

   if start <= 0 or end <= 0:
       print('Start and end must be positive')

   elif start >= end:
       print('End number must be greater than the start number')
  
   else:
       break
#Needs to be a while True statement. Confusing here but until the
    #conditions are true it won't move on. better this way so that
    #you don't have to do two different while loops. 

#print statements
print()
print('Start number: ',start)
print('End number: ',end)
print()
#for loop repeition through iterations
#needs to have plus one to be inclusive of end
for num in range(start, end+1):
  
# 1 is not a prime number, has to be above 1
    #going to go through every number
       for i in range(2,num):
           if (num%i == 0):
               break
  #if its divisible break, and repeat, if not number gets printed
       else:
           print(num)


