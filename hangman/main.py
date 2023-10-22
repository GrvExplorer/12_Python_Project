from words import words
import random
import string

def get_valid_word(wordsList):
    word = random.choice(wordsList)
    while ' ' in word or '-' in word:
        word = random.choice(wordsList)
    return word

def hangman():
    word = get_valid_word(words)
    guessed_word_right = []
    used_letter = []
    counts = 0
    live = 6
    alphabet = string.ascii_lowercase

    print(word)
    while (len(word) > counts and live > 0): # counts is words guessed correct then add 1 
        user_input = input('Guess the word: ').lower()[0]
        if (user_input in alphabet ): # input is a valid or not alphabet
            if (user_input in used_letter):
                live -= 1
                print(f'opp\'s you have used this alphabet already live left {live}')
            elif (user_input not in word):
                live -= 1
                print(f'opp\'s invalid live left {live}')

            if (user_input not in used_letter): # input already been used or not 
                used_letter.append(user_input)

        for wordarray in word: # for append the letter if it have came two times in word
            if (user_input == wordarray): # Check the input is right or not 
                guessed_word_right.append(user_input)
                counts += 1
        print()
        
        # for wordarray in word: # so that user can see which he/she have guessed and what is left 
        #     if (wordarray in guessed_word_right):
        #         print(f"{wordarray} ", end='')
        #     else:
        #         print('_ ',end='')

        word_list = [letter if letter in guessed_word_right else '_' for letter in word]
        print(' '.join(word_list))

        print()
        print("Letters used once " + ' '.join(used_letter))        # what letter have been used 
        print()

    if (live <= 0):
        print(f'Sorry you have loss the word was {word}')
    else:
        print (f'You got the word the word is {word}')
hangman()