from wordChecker import doesMeetGuidelines
from art import hangman, endMessage, introduction, clearScreen
from letterCount import getLetterCount, getCurrentStatus, insertSpaces
from termcolor import colored

# This function prints the hangman game layout to the console
def printHangman():
    print 'Current Hangman is: '
    print hangman[misses]
    print current + '\n'
    print colored("Wrong Guesses:", 'red'),
    for letter in incorrectLettersSoFar:
        print letter,
    print


# guessGuidelines should check if a user's guess is only 1 character long
# Hint: you should also check that the user's guess is not an empty string
# and does not contain uppercase letters or non-alphabetical characters...
# Have we written a function somewhere else that we can call again here?

def guessGuidelines(guess):
    # TODO: YOUR CODE HERE


# Initialize the game
clearScreen()
introduction()
correctLettersSoFar = {}
incorrectLettersSoFar = {}
misses = 0
done =  False
word = wordChecker.getWord()
letterCounts = getLetterCount(word)
current = insertSpaces(getCurrentStatus(correctLettersSoFar, word))
clearScreen()
print 'Player 2, guess the word before the goal is scored! The word is ' + str(len(word)) + ' letters long.'


# While loop should continue looping until game is over
# Hint: what boolean variables have we already defined?
while # TODO: Fill in condition
    printHangman()
    x = raw_input('\nGuess a letter: ')


    # While loop should check that user input meets guidelines
    # Hint: use the guessGuidelines function you wrote above
    while # TODO: Fill in condition
        x = raw_input('You must guess a single letter! Try again: ')
    clearScreen()


    # This series of if/elif/else statements should check the following:
    # Check that the guessed letter has not been guessed already.
    # Previous guesses have been stored in the correctLettersSoFar
    # and incorrectLettersSoFar dictionaries
    if # TODO: Fill in condition
        print 'You already guessed that! Guess again!'

    # Check if the letter guessed is in the word. Update the
    # correctLettersSoFar dictionary if it is.
    elif # TODO: Fill in condition
        # TODO: YOUR CODE HERE
        current = insertSpaces(getCurrentStatus(correctLettersSoFar, word))

        # A correct guess may be the last missing letter, revealing the whole word.
        # What comparison allows you check if all the letters have
        # been guessed correctly? Look at the dictionaries in use.
        if # TODO: Fill in condition
            printHangman()
            print 'You guessed the word correctly and saved the goal! Congratulations!'
            print endMessage
            done = True
        else:
            print 'Correct! The word contains ' + "'" + x + "'" + '. The word has been updated'

    # If the letter guessed is wrong, increment the variable counting the number
    # of guesses the user has taken. Also update the incorrectLettersSoFar dictionary
    else:
        # TODO: YOUR CODE HERE
        print 'Word does not contain ' + "'" + x + "'"


        # This block of code will be run if a guess is incorrect
        # and it is the user's 5th incorrect guess.
        if misses == 5:
            printHangman()
            guess = raw_input("\nYour final chance! Guess the word: ")

            # This if-condition should evaluate whether the user's guess of
            # the whole word is correct. One last chance to save the day!
            if # TODO: Fill in condition
                print 'You guessed the word correctly and saved the goal! Congratulations!'
                print endMessage
            else:
                print 'Sorry, the correct word is: ' + str(word)
            done = True
