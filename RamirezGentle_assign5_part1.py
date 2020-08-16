#Ramirez Gentle Assignment 5 Part 1 

ip=int(input("First octet: "))
while ip <1 or ip >255:
    print("invalid IP Address ")
    ip=int(input("First octet "))
#verification
ip2=int(input("Scond octet: "))
while ip2 <0 or ip2 >255:
    print("invalid IP Address ")
    ip2=int(input("Second octet: "))
#Verification
ip3=int(input("Third octet: "))
while ip3 <0 or ip3 >255:
    print("invalid IP Address ")
    ip3=int(input("Third octet: "))

ip4=int(input("Fourth octet: "))
while ip4 <0 or ip4 >255:
    print("invalid IP Address ")
    ip4=int(input("Fourth octet: "))
print()
#print(ip,ip2,ip3,ip4)
n=1
while n<6:
    if ip4 <255:
        ip4+=1
#Check the fourth number in the sequence first. if its zero restart
    else:
        if ip3<255:
            ip4=0
            ip3+=1
        else:
            if ip2<255:
                ip4=0
                ip3=0
                ip2+=1
            else:
                if ip<255:
                    ip4=0
                    ip3=0
                    ip2=0
                    ip+=1
    print(ip,".",ip2,".",ip3,".",ip4,sep='')
    n+=1
#stops after 5 runs                    
                
