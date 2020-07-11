month= int(input("Enter a month (1-12): "))
day= int(input("Enter a day (1-31): "))
#prompt user to enter a number for the month and prompt user to enter a number for day
#set up strings for month values
a=("January")
b=("February")
c=("March")
d=("April")
e=("May")
f=("June")
g=("July")
h=("August")
i=("September")
j=("October")
k=("November")
l=("December")

if month <1 or month > 12 or day <1 or day >31:
    print ("That's not a valid date!")
#if the month is below 1 or above 12 its not a month
#if the month is below 0 or in some cases above 31 its not a day
elif month ==1 and day <27:
    print(a,day, "is before the Spring 2020 term.")

elif month ==1 and day >27 and day <31:
    print(a, day, "is not a holiday at NYU. NYU is open on this day.")

elif month==2 and day==17:
    print(b, day, "is a holiday at NYU. NYU is not open on this day.")
elif month ==2 and day <29 and day >=1:
    print(b,day,"is not a holiday at NYU. NYU is open on this day.")

elif month ==2 and day >29 or day <1:
    print("That's not a valid date!")

if month ==3 and day >=16 and day <=22:
    print(c, day, "is Spring Break. NYU is not open on this day.")

elif month ==3 and day < 31 and day >1:
    print(c,day,"is not a holiday at NYU. NYU is open on this day.")
    
elif month ==4 and day < 30 and day >1:
    print(d,day,"is not a holiday at NYU. NYU is open on this day.")
    
elif month ==5 and day < 12 and day >1:
    print(e,day,"is not a holiday at NYU. NYU is open on this day.")

elif month ==6 and day<=30 and day <1:
    print(f,day, "is after the end of the Spring 2020 term.")

elif month ==7 and day<= 31 and day < 1:
    print(g,day, "is after the end of the Spring 2020 term.")

elif month ==8 and day<= 31 and day > 1:
    print(h,day, "is after the end of the Spring 2020 term.")

elif month ==9 and day<=31 and day > 1:
    print(i,day, "is after the end of the Spring 2020 term.")

elif month ==10 and day<=31 and day > 1:
    print(j,day, "is after the end of the Spring 2020 term.")
    
elif month ==11 and day <=30 and day > 1:
    print(k,day, "is after the end of the Spring 2020 term.")

elif month ==12 and day <=31 and day > 1:
    print(l,day, "is after the end of the Spring 2020 term.")
