import random as rd

emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}
choices = ('r', 'p', 's')

user_input = input('Rock, Paper, Scissors? (r/p/s): ').lower()
if user_input not in choices:
    print('Invalid Choice!')
    exit()

comp_choice = rd.choice(choices)

print(f'YOU CHOSE {emojis[user_input]}')
print(f'Computer CHOSE {emojis[comp_choice]}')

if user_input == comp_choice:
    print('It\'s a tie!')
elif (user_input == 's' and comp_choice == 'p') or \
     (user_input == 'r' and comp_choice == 's') or \
     (user_input == 'p' and comp_choice == 'r'):
    print('You Won!')
else:
    print('You Lost!')
