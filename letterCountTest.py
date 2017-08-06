from termcolor import colored
import letterCount

def equals(dictionary1, dictionary2):
	if len(dictionary1.keys()) != len(dictionary2.keys()):
		return False
	for key in dictionary1:
		if dictionary2[key] != dictionary1[key]:
			return False
	return True

def testCase1():
	word = "hello"
	result = letterCount.getLetterCount(word)
	answer = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
	if equals(result, answer):
		print colored('Test Case 1: Success', 'green')
	else:
		print colored("Test Case 1: Failure\nFunction: getLetterCount\nParameters: '" + word + "'", 'red')

def testCase2():
	word = "abcd"
	result = letterCount.getLetterCount(word)
	answer = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
	if equals(result, answer):
		print colored('Test Case 2: Success', 'green')
	else:
		print colored("Test Case 2: Failure\nFunction: getLetterCount\nParameters: '" + word + "'", 'red')

def testCase3():
	word = "aaaaba"
	result = letterCount.getLetterCount(word)
	answer = {'a': 5, 'b': 1}
	if equals(result, answer):
		print colored('Test Case 3: Success', 'green')
	else:
		print colored("Test Case 3: Failure\nFunction: getLetterCount\nParameters: '" + word + "'", 'red')

def testCase4():
	word = "1223434344"
	result = letterCount.getLetterCount(word)
	answer = {'1': 1, '2': 2, '3': 3, '4': 4}
	if equals(result, answer):
		print colored('Test Case 4: Success', 'green')
	else:
		print colored("Test Case 4: Failure\nFunction: getLetterCount\nParameters: '" + word + "'", 'red')

def testCase5():
	word = "Hello"
	result = letterCount.getLetterCount(word)
	answer = {'H': 1, 'e': 1, 'l': 2, 'o': 1}
	if equals(result, answer):
		print colored('Test Case 5: Success', 'green')
	else:
		print colored("Test Case 5: Failure\nFunction: getLetterCount\nParameters: '" + word + "'", 'red')

def testCase6():
	word = ""
	result = letterCount.getLetterCount(word)
	answer = {}
	if equals(result, answer):
		print colored('Test Case 6: Success', 'green')
	else:
		print colored("Test Case 6: Failure\nFunction: getLetterCount\nParameters: '" + word + "'", 'red')

def testCase7():
	word = "hello"
	correctLettersSoFar = {'h': True, 'l': True}
	result = letterCount.getCurrentStatus(correctLettersSoFar, word)
	answer = 'h-ll-'
	if result == answer:
		print colored('Test Case 7: Success', 'green')
	else:
		print colored("Test Case 7: Failure\nFunction: getLetterCount\nParameters: " + str(correctLettersSoFar) + ",'" + word + "'", 'red')

def testCase8():
	word = "hello"
	correctLettersSoFar = {}
	result = letterCount.getCurrentStatus(correctLettersSoFar, word)
	answer = '-----'
	if result == answer:
		print colored('Test Case 8: Success', 'green')
	else:
		print colored("Test Case 8: Failure\nFunction: getLetterCount\nParameters: " + str(correctLettersSoFar) + ",'" + word + "'", 'red')

def testCase9():
	word = "abcdef"
	correctLettersSoFar = {'a': True, 'b': True}
	result = letterCount.getCurrentStatus(correctLettersSoFar, word)
	answer = 'ab----'
	if result == answer:
		print colored('Test Case 9: Success', 'green')
	else:
		print colored("Test Case 9: Failure\nFunction: getLetterCount\nParameters: " + str(correctLettersSoFar) + ",'" + word + "'", 'red')

def testCase10():
	word = "a"
	correctLettersSoFar = {'a': True}
	result = letterCount.getCurrentStatus(correctLettersSoFar, word)
	answer = 'a'
	if result == answer:
		print colored('Test Case 10: Success', 'green')
	else:
		print colored("Test Case 10: Failure\nFunction: getLetterCount\nParameters: " + str(correctLettersSoFar) + ",'" + word + "'", 'red')


def testCase11():
	word = "hhhhlele"
	correctLettersSoFar = {'h': True, 'l': True}
	result = letterCount.getCurrentStatus(correctLettersSoFar, word)
	answer = 'hhhhl-l-'
	if result == answer:
		print colored('Test Case 11: Success', 'green')
	else:
		print colored("Test Case 11: Failure\nFunction: getLetterCount\nParameters: " + str(correctLettersSoFar) + ",'" + word + "'", 'red')

# Add 2 test cases below:

# def myTestCase1():

# def myTestCase2():

try:
	print '*******************************************'
	testCase1()
	print '*******************************************'
	testCase2()
	print '*******************************************'
	testCase3()
	print '*******************************************'
	testCase4()
	print '*******************************************'
	testCase5()
	print '*******************************************'
	testCase6()
	print '*******************************************'
	testCase7()
	print '*******************************************'
	testCase8()
	print '*******************************************'
	testCase9()
	print '*******************************************'
	testCase10()
	print '*******************************************'
	testCase11()
except (NotImplementedError):
	print 'Please implement the function first before running the tests!'

# Uncomment the following lines after you have written your tests
# print '*******************************************'
# myTestCase1()
# print '*******************************************'
# myTestCase2()
