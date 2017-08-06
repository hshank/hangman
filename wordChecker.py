import getpass

'''
	Function that takes in input for hangman game, confirms the user's input,
	and checks to make sure the word adheres to guidelines.
'''
def getWord():
	finished = False
	while not finished:
		word1 = getpass.getpass(prompt='Enter word: ')
		if doesMeetGuidelines(word1):
			word2 = getpass.getpass(prompt='Enter word again: ')
			if isEquals(word1,word2):
				print 'Success!'
				finished = True
			else:
				print 'Words do not match. Please try again!'
		else:
			print 'Word does not meet guidelines Please try again!'
	return word2


'''
	Given 2 words, return true if they are equal.
	Extra Condition: Ignore spaces before and after word2.

	isEquals('ghana', 'ghana    ')    =>   True
	isEquals('ghana', ' ghana')       =>   True
	isEquals('apple', 'banana')       =>   False

	HINT: use built-in function strip()
	'   abcdef  '.strip()     =>    'abcdef'

'''
def isEquals(word1, word2):
	if word1 == word2.strip():
		return True
	return False

'''
	Given a word, return true if the word adheres to the following guidelines:
		- Word cannot be empty
		- Word can only have letters in the alphabet
		- Word must be lowercase

	doesMeetGuidelines('hello')    =>    True
	doesMeetGuidelines('12heLlo')    =>    False
'''
def doesMeetGuidelines(word):
	if word == '':
		return False
	lowerCase = word.lower()
	if word != lowerCase:
		return False
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for character in word:
		if character not in alphabet:
			return False
	return True
