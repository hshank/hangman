from termcolor import colored
import wordChecker

def testCase1():
	word1 = 'hello'
	word2 = 'hello1'
	if wordChecker.isEquals(word1, word2):
		print colored("Test Case 1: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'", 'red')
	else:
		print colored('Test Case 1: Success', 'green')

def testCase2():
	word1 = 'hello'
	word2 = '  hello'
	if wordChecker.isEquals(word1, word2):
		print colored('Test Case 2: Success', 'green')
	else:
		print colored("Test Case 2: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'", 'red')

def testCase3():
	word1 = 'hello'
	word2 = 'hello  '
	if wordChecker.isEquals(word1, word2):
		print colored('Test Case 3: Success', 'green')
	else:
		print colored("Test Case 3: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'", 'red')

def testCase4():
	word1 = 'hello'
	word2 = ' hello  '
	if wordChecker.isEquals(word1, word2):
		print colored('Test Case 4: Success', 'green')
	else:
		print colored("Test Case 4: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'", 'red')

def testCase5():
	word1 = 'hello'
	word2 = 'Hello'
	if wordChecker.isEquals(word1, word2):
		print colored("Test Case 5: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'", 'red')
	else:
		print colored('Test Case 5: Success', 'green')

def testCase6():
	word1 = 'hello'
	word2 = 'abc'
	if wordChecker.isEquals(word1, word2):
		print colored("Test Case 6: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'", 'red')
	else:
		print colored('Test Case 6: Success', 'green')

def testCase7():
	word = 'hello'
	if wordChecker.doesMeetGuidelines(word):
		print colored('Test Case 7: Success', 'green')
	else:
		print colored("Test Case 7: Failure\nFunction: doesMeetGuidelines\nParameters: '" + word + "'", 'red')

def testCase8():
	word = 'hello1'
	if wordChecker.doesMeetGuidelines(word):
		print colored("Test Case 8: Failure\nFunction: doesMeetGuidelines\nParameters: '" + word + "'", 'red')
	else:
		print colored('Test Case 8: Success', 'green')

def testCase9():
	word = '12345'
	if wordChecker.doesMeetGuidelines(word):
		print colored("Test Case 9: Failure\nFunction: doesMeetGuidelines\nParameters: '" + word + "'", 'red')
	else:
		print colored('Test Case 9: Success', 'green')

def testCase10():
	word = ''
	if wordChecker.doesMeetGuidelines(word):
		print colored("Test Case 10: Failure\nFunction: doesMeetGuidelines\nParameters: '" + word + "'", 'red')
	else:
		print colored('Test Case 10: Success', 'green')

def testCase11():
	word = 'ABC#'
	if wordChecker.doesMeetGuidelines(word):
		print colored("Test Case 11: Failure\nFunction: doesMeetGuidelines\nParameters: '" + word + "'", 'red')
	else:
		print colored('Test Case 11: Success', 'green')

def testCase12():
	word = 'A'
	if wordChecker.doesMeetGuidelines(word):
		print colored("Test Case 12: Failure\nFunction: doesMeetGuidelines\nParameters: '" + word + "'", 'red')
	else:
		print colored('Test Case 12: Success', 'green')

def testCase13():
	word = ' Hello123 '
	if wordChecker.doesMeetGuidelines(word):
		print colored("Test Case 13: Failure\nFunction: doesMeetGuidelines\nParameters: '" + word + "'", 'red')
	else:
		print colored('Test Case 13: Success', 'green')

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
	print '*******************************************'
	testCase12()
	print '*******************************************'
	testCase13()
except (NotImplementedError):
	print 'Please implement the function first before running the tests!'

# Uncomment the following lines after you have written your tests
# print '*******************************************'
# print myTestCase1()
# print '*******************************************'
# print myTestCase2()
