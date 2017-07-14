def remove_duplicates(word):
	dic = {}
	ret = ''
	for elem in word:
		if elem not in dic:
			dic[elem] = True
			ret = ret + elem
	return ret


 

hangman = {}
hangman[0] = "   ____\n  |    |    \n  |         \n  |     \n  |    \n  |   \n _|_\n|   |\n"
hangman[1] = "   ____\n  |    |    \n  |    o    \n  |     \n  |    \n  |   \n _|_\n|   |\n"
hangman[2] = "   ____\n  |    |    \n  |    o    \n  |   /  \n  |    \n  |   \n _|_\n|   |_\n"
hangman[3] = "   ____\n  |    |    \n  |    o    \n  |   / \ \n  |    \n  |   \n _|_\n|   |\n"
hangman[4] = "   ____\n  |    |    \n  |    o    \n  |   /|\ \n  |    |\n  |   /\n _|_\n|   |\n"
hangman[5] = "   ____\n  |    |    \n  |    o    \n  |   /|\ \n  |    |\n  |   \n _|_\n|   |\n"
hangman[6] = "   ____\n  |    |    \n  |    o    \n  |   /|\ \n  |    |\n  |   / \ \n _|_\n|   |\n"



# print 'Welcome to Hangman'


word = raw_input('Player 1: please type the word that you want Player 2 to guess: ')
print chr(27) + "[2J"


print 'Thanks! Player 2, it is your turn to start guessing letters!'


count = len(word)


dic = {}
count = 0
for elem in remove_duplicates(word):
	dic[elem] = count
	count += 1

correct = {}

wrong_count = 0
i = 0
done =  False
ret = ''
for elem in word:
	ret = ret + '- '
while i < count and not done:
	print 'Current Hangman is: '
	print hangman[wrong_count]
	letter = raw_input('Guess a letter here: ')
	print chr(27) + "[2J"

	x = letter
	if x in correct:
		print '\n\n\n You already guessed that! Guss again!'
	else:
		if x in dic:
			print '\n\n\nYup! You got it. THe word has been updated\n\n\n\n'
			correct[x] = True
			ret = ''
			for elem in word:
				if elem in correct:
					ret = ret + elem
				else:
					ret = ret + '-'
				ret = ret + ' '
			print ret
			if len(correct.keys()) == len(dic.keys()):
				print 'done'
				done = True
		else:
			wrong_count += 1
			print '\n\n\WRONG! Word does not contain this\n\n\n\n'
			
			if wrong_count == 6:
				print hangman[wrong_count]				
				guess = raw_input("Guess the word! Your final chance!\n FOr your reference so far you have " + ret + "\n")
				if guess == word:
					print 'sucess!!!'
					done = True
				else:
					print 'sorry that is incorrect.'
					print 'correct word is: ' + str(word)
					done = True
			


