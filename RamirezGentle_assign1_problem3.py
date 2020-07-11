#RamirezGentle Assignment 1 Problem 3

#insert names 
user_name1 = input ('Please enter name #1 ')
user_name2 = input ('Please enter name #2 ')
user_name3 = input ('Please enter name #3 ')

#printing Out put statements

print('Here are your names in every possible order:')
print('---------------------------------------------')
print(user_name1, user_name2, user_name3, sep=', ') 
print(user_name1, user_name3, user_name2, sep=', ')
print(user_name2, user_name1, user_name3, sep=', ')
print(user_name2, user_name3, user_name1, sep=', ')
print(user_name3, user_name2, user_name1, sep=', ')
print(user_name3, user_name1, user_name2, sep=', ')
