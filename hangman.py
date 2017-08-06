import wordChecker
import letterCount
import os

hangman = {}
hangman[0] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n\n    o\n  -()-\n   |\_o\n\n'
hangman[1] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n\n    o     \n  -()-    o\n   |\_\n'
hangman[2] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n           o\n    o     \n  -()-  \n   |\_\n'
hangman[3] = '           ________________\n          |################|\n          |################|\n          |################|\n\n                      o\n\n    o     \n  -()-  \n   |\_\n'
hangman[4] = '           ________________\n          |################|\n          |################|\n          |################|\n                      o\n\n\n    o     \n  -()-  \n   |\_\n'
hangman[5] = '           ________________\n          |       GOAL     |\n          |      GOAL    o |\n          |      GOAL      |\n\n\n\n    o     \n  -()-  \n   |\_\n'
endMessage = '_________                                     __           ._.\n\_   ___ \  ____   ____    ________________ _/  |_  ______ | |\n/    \  \/ /  _ \ /    \  / ___\_  __ \__  \\   __\/  ___/ | |\n\     \___(  <_> )   |  \/ /_/  >  | \// __ \|  |  \___ \   \|\n \______  /\____/|___|  /\___  /|__|  (____  /__| /____  >  __\n        \/            \//_____/            \/          \/   \/'

def clearScreen():
    os.system("clear")

def guessGuidelines(guess):
    if wordChecker.doesMeetGuidelines(guess):
        if len(guess) == 1:
            return True
    return False


# Initialize the game
correctLetterSoFar = {}
incorrectLetterSoFar = {}
misses = 0
done =  False
word = wordChecker.getWord()
letterCounts = letterCount.getLetterCount(word)
current = letterCount.getCurrentStatus(correctLetterSoFar, word)
clearScreen()

print 'Welcome to Hangman - Sports Edition!\n'
while not done:
    print 'Current Hangman is: '
    print hangman[misses]
    print current + '\n'
    x = raw_input('Guess a letter: ')
    while not guessGuidelines(x):
        x = raw_input('You must guess a single letter! Try again: ')
    clearScreen()

    if x in correctLetterSoFar or x in incorrectLetterSoFar:
        print 'You already guessed that! Guess again!'
    elif x in letterCounts:
        correctLetterSoFar[x] = True
        current = letterCount.getCurrentStatus(correctLetterSoFar, word)
        if len(correctLetterSoFar.keys()) == len(letterCounts.keys()):
            print current + '\n'
            print 'You guessed the word correctly and protected the goal! Congratulations!'
            print endmessage
            done = True
        else:
            print 'Correct! The word contains ' + "'" + x + "'" + '. The word has been updated'
    else:
        misses += 1
        incorrectLetterSoFar[x] = True
        print 'Word does not contain ' + "'" + x + "'"

        if misses == 5:
            print hangman[misses]
            print current + '\n'
            guess = raw_input("Your final chance! Guess the word: ")
            if guess == word:
                print 'You guessed the word correctly and protected the goal! Congratulations!'
                print endMessage
            else:
                print 'Sorry, the correct word is: ' + str(word)
            done = True
