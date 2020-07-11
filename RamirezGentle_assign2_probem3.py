

#RamirezGentle_assign2_problem3

bit=8
byte=1024
giga= byte*byte
#setup for conversions
num_size= float(input("Enter a file size, in kilobyes (KB): "))
#get input as a float
#you would mess this up with a runtime error if a number is not givenRUNTIME
#you would mess this up with a syntax error with a wrong apostropheSYNTAX
byte_1 =(num_size*bit*byte)
byte_2= (num_size*byte)
byte_3= (num_size/byte)
#you would crash this program with the wrong opperations LOGIC
byte_4= (num_size/giga)
#convert from bits all the way to giga bites
w1=format(byte_1,',.2f')
x1=format(byte_2, ',.2f')
y1=format(byte_3,',.2f')
z1=format(byte_4,',.2f')
#you would mess with the the wrong apostrophes SYNTAX
#format numbers to decimals and commas
w2=str(w1) 
x2=str(x1)
y2=str(y1)
z2=str(z1)
#make them strings so you can align them
w=format(w2,'>25s')
x=format(x2, '>24s')
y=format(y2, '>20s')
z=format(z2, '>20s')
#YOU WOULD MESS THIS UP WITH THE WRONG APOSTROPHE SYNTAX
#print statements
print()
print(num_size, "KB ...")
print()
print("... in bits", w, "bits")
print("... in bytes",x,"bytes")
print("... in megabytes", y,"MB")
print("... in gigabytes", z,"GB")
