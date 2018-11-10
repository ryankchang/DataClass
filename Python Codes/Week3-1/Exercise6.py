condition = 'y'
initial = 0

while condition == 'y':
    user_input = int(input('How many numbers? '))
    for i in range(initial, initial + user_input):
        print(i)
        initial += user_input
    condition = input("Continue? [y/n]")
