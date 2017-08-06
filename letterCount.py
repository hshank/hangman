'''
	Given a word, return a dictionary where each key is a letter in word and the value is the number of times
	it appears in the word.

	getLetterCount('hello')    =>      {'h': 1, 'e': 1, 'l', 2, 'o'}
	getLetterCount('aabbcdc')  =>      {'a': 2, 'b': 2, 'c': 2, 'd': 1}
'''
def getLetterCount(word):
	dictionary = {}
	for letter in word:
		if letter in dictionary:
			dictionary[letter] += 1
		else:
			dictionary[letter] = 1
	return dictionary


'''
	Construct a new string that is exactly like word, except for letters that do not appear in correctLetterSoFar
	should be replaced by a '-'.

	Make sure to put a space in between each letter in the returned string

	getCurrentStatus({'h': True, 'l': True}, 'hello')     =>    'h - l l -'
'''
def getCurrentStatus(correctLettersSoFar, word):
	currentStatus = ''
	for letter in word:
		if letter in correctLettersSoFar:
			currentStatus = currentStatus + letter
		else:
			currentStatus = currentStatus + '-'
	return currentStatus


'''
	Given a string, return a string that has spaces in between the characters.
'''
def insertSpaces(word):
	returnString = word[0]
	for elem in word[1:]:
		returnString +=  ' ' + elem
	return returnString
