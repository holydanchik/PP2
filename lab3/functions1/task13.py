from random import randrange

def game (guess, number):
    i = 1
    while (guess != number):
        print('Take a guess.')
        guess = int(input())
        print()
        if guess == number:
            print('Good job, ' + name + '! You guessed my number in', i, 'guesses!')
        elif guess>number:
            i += 1
            print('Your guess is too high.')
        elif number>guess:
            i += 1
            print('Your guess is too low.')
    

print('Hello! What is your name?')
name = input()
print()
print("Well, " + name + ", I am thinking of a number between 1 and 20.")


number = randrange(1, 20)
guess = 21

game(guess, number)