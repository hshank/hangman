import wordChecker
import letterCount

hangman = {}
hangman[0] = "   ____\n  |    |    \n  |         \n  |     \n  |    \n  |   \n _|_\n|   |\n"
hangman[1] = "   ____\n  |    |    \n  |    o    \n  |     \n  |    \n  |   \n _|_\n|   |\n"
hangman[2] = "   ____\n  |    |    \n  |    o    \n  |   /  \n  |    \n  |   \n _|_\n|   |_\n"
hangman[3] = "   ____\n  |    |    \n  |    o    \n  |   / \ \n  |    \n  |   \n _|_\n|   |\n"
hangman[4] = "   ____\n  |    |    \n  |    o    \n  |   /|\ \n  |    |\n  |   /\n _|_\n|   |\n"
hangman[5] = "   ____\n  |    |    \n  |    o    \n  |   /|\ \n  |    |\n  |   \n _|_\n|   |\n"
hangman[6] = "   ____\n  |    |    \n  |    o    \n  |   /|\ \n  |    |\n  |   / \ \n _|_\n|   |\n"


print 'Welcome to Hangman'
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
		
		if misses == 6:
			print hangman[misses]				
			guess = raw_input("Guess the word! Your final chance!\n FOr your reference so far you have " + current + "\n")
			if guess == word:
				print 'Success!!!'
				done = True
			else:
				print 'sorry that is incorrect.'
				print 'correct word is: ' + str(word)
				done = True
			


