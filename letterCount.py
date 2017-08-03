def getLetterCount(word):
	dictionary = {}
	for character in word:
		if character in dictionary:
			dictionary[character] += 1
		else:
			dictionary[character] = 1
	return dictionary

def getCurrentStatus(correct, word):
	currentStatus = ''
	for character in word:
		if character in correct:
			currentStatus = currentStatus + character
		else:
			currentStatus = currentStatus + '-'
		currentStatus = currentStatus + ' '
	return currentStatus