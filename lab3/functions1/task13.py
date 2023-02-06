from random import randrange

def game (guess, number, count):
    print('Take a guess.')
    guess = int(input())
    print()
    if guess == number:
        print('Good job, ' + name + '! You guessed my number in', count,  'guesses!')
    else:
        print('Your guess is too high.') if number<guess else print('Your guess is too low.') 
        game(guess, number, count+1)
    
print('Hello! What is your name?')
name = input()
print()
print("Well, " + name + ", I am thinking of a number between 1 and 20.")

number = randrange(1, 20)
guess = 21

game(guess, number, 1)