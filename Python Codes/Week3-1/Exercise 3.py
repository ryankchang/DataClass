my_first = input('What is your first name? ')
his_first = input("What is your partner's name? ")
my_time = input('How many months have you been coding? ')
his_time = input('How many months has your partner been coding? ')

total_time = int(my_time) + int(his_time)

print(f'{my_first} has been coding for {my_time} months. {his_first} has been coding for {his_time} months.')
print(f'Together we have been coding for {total_time} months!')
