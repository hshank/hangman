def getWord():
	finished = False
	while not finished:
		word1 = raw_input('Enter word: ')
		if doesMeetGuidelines(word1):
			word2 = raw_input('Enter word again: ')
			if isEquals(word1,word2):
				print 'Success!'
				finished = True
			else:
				print 'Words do not match. Please try again!'
		else:
			print 'Word does not meet guidelines Please try again!'
	return word2

def isEquals(word1, word2):
	if word1 == word2:
		return True
	return False


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
