import random

def guess(x):
    randomNum = random.randint(1, x)
    guess = 0
    while guess != randomNum:
        guess = int(input('Guess the number: '))
        print()
        if (guess < randomNum):
           print('It is too Low')
        elif (guess > randomNum):
            print('It\'s too High')
    print('comratulation')

def computerGuess(x):
     low = 1
     high = x
     setGuess = random.randint(low, high)
     feedback = ''
     while (feedback != 'c') :
        guess = random.randint(low, high) # if low == high then also no error 
        if (guess < setGuess):     
            low = guess + 1
            print(guess)
            print('too low')
        elif (guess > setGuess):
            high = guess - 1 
            print(guess)
            print('too high')
        elif (guess == setGuess):
            feedback = 'c'
            print(guess)
            print('comratulation')
        print()
     print(setGuess)

def computer_guess_usingInput(x):
     low = 1
     high = x
     feedback = ''
     while (feedback != 'c') :
        guess = random.randint(low, high) # if low == high then also no error 
        feedback = input(f'Input {guess} too low (l) too high (h) correct (c): ').lower()[0]
        if (feedback == 'l'):     
            low = guess + 1
        elif (feedback == 'h'):
            high = guess - 1 
        print()
     print(f'Yay! computer have guessed you secret number {guess}')

