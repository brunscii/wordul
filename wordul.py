'''
Author: Chris Carlin

This is a wordle knock off that runs in the terminal
it prints out either a thubs up or down for the letter being correct or incorrect
    
I created a list of 5 letter words that are suitable for the game

TODO: 
Add a feature to take any file and return a set of 5 letter words to be used by the game
'''

import random

def print_instructions():
    print('''\n\rThis is a knock off or wordle for the command line
I will randomly choose a 5 letter word
You will guess the word
I will then mark the correct letters with 👍 and incorrect with .👎
If you are in windows please use the powershell or windows terminal 
------------------------------------------------------------------------'''
    )


def load_words(fname):
    words = []
    with open(fname) as word_file:
        words = word_file.readlines()
        
    return words

def grab_word(words):
    return random.choice(words)

def play(word):

    guesses = 6
    while(guesses > 0):
        correct_letters = '          '
        try:
            guess = str(input('Enter a guess: ')).lower()
        except KeyboardInterrupt:
            exit()
        if len(guess)!=5:
            continue
        if guess != word:

            letters = ''
            for letter1, letter2 in zip(word, guess):
                if letter1 == letter2:
                    letters = letters + '👍'
                    pos = word.index(letter1)*2+1
                    correct_letters = correct_letters[:pos] + letter1 + correct_letters[pos:] 
                    #print('👍', end = '')
                else:
                    letters = letters + '👎'
                    #print('👎', end = '')
            print('')
            print(correct_letters)
            print(letters)
            guesses = guesses - 1
        else:
            print('')
            print(f' {word[0]} {word[1]} {word[2]} {word[3]} {word[4]}')
            print('👍👍👍👍👍')
            print('Sunofagun you gots it')
            return True
    
    print(f"The correct word was {word}")
    return False
        
if __name__ == "__main__":
    
    print_instructions()
    words = load_words('words5.txt')
    word = str(grab_word(words)).lower()
    while('/' in word):
        word = grab_word()
    play(word)


    
