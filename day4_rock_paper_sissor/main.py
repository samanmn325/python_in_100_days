import random

l = ['rock', 'papar', 'scissor']
count = 'y'
while count == 'y':
    print(l)
    my_choice = str(input("your choice:"))
    bot_choice = l[random.randint(0, 2)]
    print(f"your choice is '{my_choice}'")
    print(f"bot choice is '{bot_choice}'")
    if my_choice == 'rock' or my_choice == 'paper' or my_choice == 'scissor':
        if my_choice == 'rock':
            if bot_choice == 'rock':
                print("it's a draw!")
            elif bot_choice == 'papar':
                print('bot wins!')
            else:
                print('you win!')

        elif my_choice == 'papar':
            if bot_choice == 'rock':
                print("you win!")
            elif bot_choice == 'papar':
                print("it's a draw!")
            else:
                print('bot wins!')

        else:
            if bot_choice == 'rock':
                print("bot wins!")
            elif bot_choice == 'papar':
                print('you win!')
            else:
                print("it's a draw!")

    else:
        print('try again!')
    count = str(input("type 'y' to continue  ,'n' to exit: "))
