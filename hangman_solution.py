from wordChecker_solution import doesMeetGuidelines, getWord
from art import hangman, endMessage, introduction, clearScreen
from letterCount_solution import getLetterCount, getCurrentStatus, insertSpaces
from termcolor import colored

def printHangman():
    print 'Current Hangman is: '
    print hangman[misses]
    print current + '\n'
    print colored("Wrong Guesses:", 'red'),
    for letter in incorrectLettersSoFar:
        print letter,
    print

def guessGuidelines(guess):
    if doesMeetGuidelines(guess):
        if len(guess) == 1:
            return True
    return False


clearScreen()
introduction()
correctLettersSoFar = {}
incorrectLettersSoFar = {}
misses = 0
done =  False
word = getWord()
letterCounts = getLetterCount(word)
current = insertSpaces(getCurrentStatus(correctLettersSoFar, word))
clearScreen()
print 'Player 2, guess the word before the goal is scored! The word is ' + str(len(word)) + ' letters long.'


while not done:
    printHangman()
    x = raw_input('\nGuess a letter: ')
    while not guessGuidelines(x):
        x = raw_input('You must guess a single letter! Try again: ')
    clearScreen()

    if x in correctLettersSoFar or x in incorrectLettersSoFar:
        print 'You already guessed that! Guess again!'
    elif x in letterCounts:
        correctLettersSoFar[x] = True
        current = insertSpaces(getCurrentStatus(correctLettersSoFar, word))
        if len(correctLettersSoFar.keys()) == len(letterCounts.keys()):
            printHangman()
            print 'You guessed the word correctly and saved the goal! Congratulations!'
            print endMessage
            done = True
        else:
            print 'Correct! The word contains ' + "'" + x + "'" + '. The word has been updated'
    else:
        misses += 1
        incorrectLettersSoFar[x] = True
        print 'Word does not contain ' + "'" + x + "'"

        if misses == 5:
            printHangman()
            guess = raw_input("\nYour final chance! Guess the word: ")
            if guess == word:
                print 'You guessed the word correctly and saved the goal! Congratulations!'
                print endMessage
            else:
                print 'Sorry, the correct word is: ' + str(word)
            done = True
