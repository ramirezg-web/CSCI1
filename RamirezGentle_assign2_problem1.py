#RamirezGentle_assign2_problem1


print("Hello! I'm here to help you calculate your tip. ")
bill= float(input("How much was your bill? \
(enter as a number without dollar signs or commas): $"))
tip= float(input("How much tip would you like to leave? \
(enter just a number): "))
tip_1= round((tip*.01)*bill,2)
tip_2=tip_1+bill
#Calculate tips and print tip amount them add
print("Thanks!")
print("You need to leave $", format((tip_1), '.2f'), " as a tip.", sep='')
print("Your total bill will be $", round(tip_2,2), '.', sep='')
