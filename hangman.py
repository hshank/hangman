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

word = wordChecker.getWord()
letterCounts = letterCount.getLetterCount(word)


correctLetterSoFar = {}
misses = 0
done =  False
current = letterCount.getCurrentStatus(correctLetterSoFar, word)
while not done:
    print 'Current Hangman is: '
    print hangman[misses]
    print current
    letter = raw_input('Guess a letter here: ')
    print chr(27) + "[2J"

    x = letter
    if x in correctLetterSoFar:
        print '\n\n\n You already guessed that! Guess again!'
    elif x in letterCounts:
        correctLetterSoFar[x] = True
        current = letterCount.getCurrentStatus(correctLetterSoFar, word)
        if len(correctLetterSoFar.keys()) == len(letterCounts.keys()):
            print 'You won!'
            done = True
            print current
        else:
            print '\n\n\nYup! You got it. The word has been updated\n\n\n\n'
            print current
    else:
        misses += 1
        print '\n\nWRONG! Word does not contain this\n\n\n\n'
        
        if misses == 5:
            print hangman[misses]               
            guess = raw_input("Guess the word! Your final chance!")
            print current
            if guess == word:
                print 'Success!!!'
                done = True
            else:
                print 'sorry that is incorrect.'
                print 'correct word is: ' + str(word)
                done = True
            
