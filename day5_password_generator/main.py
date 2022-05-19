import random

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-']

print('welcome to the pyPassword generator!')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input(f'How many symbols would you like? \n'))
nr_numbers = int(input(f'How many numbers would you like? \n'))

# password = ''
# for i in range(0 , nr_letters ):
#     print(i)
#     rand = letter[random.randint(0,len(letter) -1)]
#     password += rand
# for i in range(0 , nr_numbers ):
#     print(i)
#     rand = number[random.randint(0,len(number) - 1)]
#     password += rand
# for i in range(0 , nr_symbols ):
#     print(i)
#     rand = symbol[random.randint(0,len(symbol) - 1)]
#     password += rand
# print(password)

password2 = []
for i in range(0, nr_letters):
    password2.append(random.choice(letter))
for i in range(0, nr_numbers):
    password2.append(random.choice(number))
for i in range(0, nr_symbols):
    password2.append(random.choice(symbol))
print(password2)
random.shuffle(password2)
print(password2)
