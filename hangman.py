import wordChecker
import letterCount

hangman = {}
hangman[0] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n\n    o\n  -()-\n   |\_o\n\n'
hangman[1] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n\n    o     \n  -()-    o\n   |\_\n'
hangman[2] = '           ________________\n          |################|\n          |################|\n          |################|\n\n\n           o\n    o     \n  -()-  \n   |\_\n'
hangman[3] = '           ________________\n          |################|\n          |################|\n          |################|\n\n                      o\n\n    o     \n  -()-  \n   |\_\n'
hangman[4] = '           ________________\n          |################|\n          |################|\n          |################|\n                      o\n\n\n    o     \n  -()-  \n   |\_\n'
hangman[5] = '           ________________\n          |       GOAL     |\n          |      GOAL    o |\n          |      GOAL      |\n\n\n\n    o     \n  -()-  \n   |\_\n'

print 'Welcome to Hangman - Sports Edition!\n'

def clearScreen():
    print chr(27) + "[2J"


word = wordChecker.getWord()
letterCounts = letterCount.getLetterCount(word)


correctLetterSoFar = {}
misses = 0
done =  False
current = letterCount.getCurrentStatus(correctLetterSoFar, word)
while not done:
    print 'Current Hangman is: '
    print hangman[misses]
    print current + '\n'
    letter = raw_input('Guess a letter here: ')
    clearScreen()

    x = letter
    if x in correctLetterSoFar:
        print '\n\n\nYou already guessed that! Guess again!'
    elif x in letterCounts:
        correctLetterSoFar[x] = True
        current = letterCount.getCurrentStatus(correctLetterSoFar, word)
        if len(correctLetterSoFar.keys()) == len(letterCounts.keys()):
            print 'You guessed the word correctly and saved the goal! Congratulations!'
            print current + '\n'
            done = True
        else:
            print '\n\n\nCorrect! The word contains ' + x + '. The word has been updated'
    else:
        misses += 1
        print '\n\n\nWord does not contain ' + x
        
        if misses == 5:
            print hangman[misses]               
            guess = raw_input("Guess the word! Your final chance!")
            print current + '\n'
            if guess == word:
                print 'Success!!!'
                done = True
            else:
                print 'Sorry that is incorrect.'
                print 'The correct word is: ' + str(word)
                done = True
            
