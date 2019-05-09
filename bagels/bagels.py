from random import randint
import os

os.system('clear')

def bagels():
    print('''I am thinking of a 3-digit number. Try to guess what it is.
The clues I give are...
When I say:    That means:
    Bagels       None of the digits is correct.
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
I have thought up a number. You have 10 guesses to get it.
''')
    a = randint(1,9)
    b = randint(0,9)
    c = randint(0,9)
    solution = [a,b,c]
    guesses = 0
    solved = False
    
    print(solution,f'{a}{b}{c}')

    while solved == False and guesses < 10:
        guess = input('3 digit number: ')
        guess_list = [int(guess[0]), int(guess[1]), int(guess[2])]
        print(guess_list)
        for num in guess_list:
            if num in solution:
                print('Ok')

bagels()