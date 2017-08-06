def getLetterCount(word):
	dictionary = {}
	for letter in word:
		if letter in dictionary:
			dictionary[letter] += 1
		else:
			dictionary[letter] = 1
	return dictionary


def getCurrentStatus(correctLettersSoFar, word):
	currentStatus = ''
	for letter in word:
		if letter in correctLettersSoFar:
			currentStatus = currentStatus + letter
		else:
			currentStatus = currentStatus + '-'
	return currentStatus


def insertSpaces(word):
	returnString = word[0]
	for elem in word[1:]:
		returnString +=  ' ' + elem
	return returnString
