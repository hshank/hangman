# Given a word, return a dictionary where each key is a letter in word and the
# value is the number of times it appears in the word.
#
# getLetterCount('hello')    =>      {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# getLetterCount('aabbcdc')  =>      {'a': 2, 'b': 2, 'c': 2, 'd': 1}

def getLetterCount(word):
	dictionary = {}

	# TODO: YOUR CODE HERE
	# Remove the "raise" line below once you begin writing your solution
	raise NotImplementedError

	return dictionary



# Construct a new string that is exactly like word, except for letters that do
# not appear in correctLetterSoFar should be replaced by a '-'.
#
# getCurrentStatus({'h': True, 'l': True}, 'hello')     =>    'h - l l -'

def getCurrentStatus(correctLettersSoFar, word):
	newString = ''

	# TODO: YOUR CODE HERE
	# Remove the "raise" line below once you begin writing your solution
	raise NotImplementedError

	return newString


# Given a string, return a string that has spaces in between the characters.
def insertSpaces(word):
	returnString = word[0]
	for elem in word[1:]:
		returnString +=  ' ' + elem
	return returnString
