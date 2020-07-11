#RamirezGentle Assignment 3 Problem 1
print("Valid Triangle Tester")
#print Statement
x1= float(input("Enter Point #1 - x position: "))
y1= float(input("Enter Point #1 - y position: "))
x2= float(input("Enter Point #2 - x position: "))
y2= float(input("Enter Point #2 - y position: "))
x3= float(input("Enter Point #3 - x position: "))
y3= float(input("Enter Point #3 - y position: "))
#prompt user to enter 3 points on a standard cartesian plane. 

side1= ((x1-x2)**2 + (y1-y2)**2)**0.5
side2= ((x2-x3)**2 + (y2-y3)**2)**0.5
side3= ((x3-x1)**2 + (y3-y1)**2)**0.5
#compute the distance between each point. Computing 3 distance values
print()
print("The length of each side of your test shape is: ")
print("Side 1: ",format((side1),'.2f'))
print("Side 2: ",format((side2), '.2f'))
print("Side 3: ",format((side3), '.2f'))
print()
#report distance to the user rounded to 2 decimal places
if side1+side2> side3 and side2+side3>side1 and side1+side3>side2:
    print("This is a valid triangle!")
#if under these conditions report its a valid triangle
else:
    print("This is not a valid triangle")
