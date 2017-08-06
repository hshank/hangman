import wordChecker
import os
from art import hangman, endMessage
from letterCount import getLetterCount, getCurrentStatus, insertSpaces

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
letterCounts = getLetterCount(word)
current = insertSpaces(getCurrentStatus(correctLetterSoFar, word))
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
        current = insertSpaces(getCurrentStatus(correctLetterSoFar, word))
        if len(correctLetterSoFar.keys()) == len(letterCounts.keys()):
            print current + '\n'
            print 'You guessed the word correctly and protected the goal! Congratulations!'
            print endMessage
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
