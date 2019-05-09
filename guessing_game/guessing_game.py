from random import randint

def guessing_game():
    number_to_guess = randint(1,1000)
    number_of_guesses = 0
    solved = False
    previous_guesses = []
    name = input('What is your name: ') or 'PlayerOne'
    print(f"Well {name}, let's play a game.  I'm thinking of a number between 1 and 1000.  I'll give you 9 guesses to get it right.")
    print(number_to_guess)
    while solved == False and number_of_guesses < 10:
        if len(previous_guesses) > 0:
            print(f'Previous guesses: {previous_guesses}')

        guess = int(input('Guess a number: '))
        
        if guess == number_to_guess and number_of_guesses == 0:
            print(f'Holy cow!!! You guessed {guess} and got it on your first guess!!!')
            solved = True
        elif guess == number_to_guess:
            number_of_guesses += 1
            print(f'Bingo! You guessed {guess} and that was the right number. You took {number_of_guesses} guesses!')
            solved = True
        elif guess > number_to_guess:
            number_of_guesses += 1
            previous_guesses.append(guess)
            print(f'Too high! Guesses: {number_of_guesses}')
        else:
            number_of_guesses += 1
            previous_guesses.append(guess)
            print(f'Too low! Guesses: {number_of_guesses}')
    if number_of_guesses == 10 and solved == False:
        print(f'Game over {name}!!! That was your last guess.')

guessing_game()