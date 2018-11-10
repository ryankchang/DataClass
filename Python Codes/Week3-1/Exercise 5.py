import random
possible = ['rock','paper','scissors']

continue_code = 'y'

while continue_code == 'y':

    user = input('Pick one - [rock | paper | scissors]: ')
    computer = random.choice(possible)

    if user not in possible:
        print('Please select a valid choice. {user} is not valid.')

    print(f'You picked {user}. Computer picked {computer}.')

    if user == 'rock':
        if computer == 'paper':
            print('Computer wins :(')
        elif computer == 'rock':
            print("Try again")
        elif computer == 'scissors':
            print("You win!")
    elif user == 'scissors':
        if computer == 'paper':
            print('You win!')
        elif computer == 'rock':
            print("Computer wins :(")
        elif computer == 'scissors':
            print("You win!")
    elif user == 'paper':
        if computer == 'paper':
            print('Try again')
        elif computer == 'rock':
            print("You win!")
        elif computer == 'scissors':
            print("Computer wins :(")

    continue_code = input("Continue? [y/n]: ")


