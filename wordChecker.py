import getpass

# Function that takes in input for hangman game, confirms the user's input,
# and checks to make sure the word adheres to guidelines.

def getWord():
	finished = False
	while not finished:
		word1 = getpass.getpass(prompt='\nEnter word: ')
		if doesMeetGuidelines(word1):
			word2 = getpass.getpass(prompt='\nEnter word again: ')
			if isEquals(word1, word2):
				finished = True
			else:
				print 'Words do not match. Please try again!'
		else:
			print 'Word does not meet guidelines. Please try again!'
	return word2


# Given 2 words, return True if they are equal.
# Extra Condition: Ignore spaces before and after word2.

# isEquals('ghana', 'ghana    ')    =>   True
# isEquals('ghana', ' ghana')       =>   True
# isEquals('apple', 'banana')       =>   False
#
# HINT: use built-in function strip(), which removes all spaces in a string
# '   abcdef  '.strip()     =>    'abcdef'

def isEquals(word1, word2):
	# TODO: YOUR CODE HERE

	# Remove the "raise" line below once you begin writing your solution
	raise NotImplementedError

	return True


# Given a word, return True if the word adheres to the following guidelines:
# 	- Word cannot be empty
# 	- Word can only have letters in the alphabet
# 	- Word must be lowercase
#
# doesMeetGuidelines('hello')    =>    True
# doesMeetGuidelines('12heLlo')    =>    False
#
# HINT: Some built-in functions that will help you are:
#		-  lower() --> returns a lowercase-only version of a string. Examples:
#		   'hello'.lower() = 'hello'
#		   'HELLO'.lower() = 'hello'
#
#		-  isalpha() --> returns true if a string is made up of only
#		   alphabetical characters. Examples:
#		   'hey'.isalpha() = True
#		   '123'.isalpha() = False

def doesMeetGuidelines(word):
	# TODO: YOUR CODE HERE

	# Remove the "raise" line below once you begin writing your solution
	raise NotImplementedError

	return True
