#RamirezGentle_assign2_problem2

num_cost= float(input("Enter cost price: "))
num_sale= float(input("Enter sales prices: "))
num_sold= float(input("Enter inventory sold: "))
#input all data
prof= (num_sold*num_sale)-(num_sold*num_cost)
#calculate
prof_marg= (num_sale-num_cost)/num_sale
print()
print("You made a profit of $",(format(prof,',.0f')),sep='',end='.') 
print()
print("Your profit margin is ",(format(prof_marg,'.1%')),sep='', end='.')
