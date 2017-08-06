import getpass

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


def isEquals(word1, word2):
	if word1 == word2.strip():
		return True
	return False


def doesMeetGuidelines(word):
	if word == '':
		return False
	if not word.isalpha():
		return False
	if word != word.lower():
		return False
	return True
