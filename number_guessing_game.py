import random


print('============= Welocme To Guessing Game =============')
print('- You have 3 chances to guess the number between 1-100')

def difficult():
    print('- Choose the difficulty:')
    print('                        1. Eazy   (10 chances)')
    print('                        2. Medium (5 chances)')
    print('                        3. Hard   (3 chances)')
    
    difficulty = input('\n-> Enter the level: ')
    
    chances = 0
    level = ''
    if difficulty == '1':
        level = 'eazy'
        chances = 10
    elif difficulty == '2':
        level = 'medium'
        chances = 5
    elif difficulty == '3':
        level = 'hard'
        chances = 3
    else:
        print('Wrong input, Try again')
        return difficult()
    
    print(f'\nGreat you now in the {level} level\nLest start\n\n')
    return chances
    

chances = difficult()
num = random.randint(0,101)

while chances > 0:
    guess = int(input('Your guess: '))
    
    if guess == num:
        break
    
    chances -= 1
    
    if guess > num:
        print(f'==> Too big, still {chances} chance')
    elif guess < num:
        print(f'==> Too small, still {chances} chance')
    
if chances == 0:
    print('You runs Out of chances, Try again!!')
else:
    print(f'You Won!!!, you still have {chances} of your chances')