import wordChecker

def testCase1():
	word1 = 'hello'
	word2 = 'hello1'
	if wordChecker.isEquals(word1, word2):
		return 'Test Case 1: Success'
	return "Test Case 1: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'"

def testCase2():
	word1 = 'hello'
	word2 = '  hello'
	if wordChecker.isEquals(word1, word2):
		return 'Test Case 2: Success'
	return "Test Case 2: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'"

def testCase3():
	word1 = 'hello'
	word2 = 'hello  '
	if wordChecker.isEquals(word1, word2):
		return 'Test Case 3: Success'
	return "Test Case 3: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'"

def testCase4():
	word1 = 'hello'
	word2 = ' hello  '
	if wordChecker.isEquals(word1, word2):
		return 'Test Case 4: Success'
	return "Test Case 4: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'"

def testCase5():
	word1 = 'hello'
	word2 = 'Hello'
	if wordChecker.isEquals(word1, word2):
		return "Test Case 5: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'"
	return 'Test Case 5: Success'

def testCase6():
	word1 = 'hello'
	word2 = 'abc'
	if wordChecker.isEquals(word1, word2):
		return "Test Case 6: Failure\nFunction: isEquals\nParameters: '" + word1 + "','" + word2 + "'"
	return 'Test Case 6: Success'

def testCase7():
	word = 'hello'
	if wordChecker.doesMeetGuidelines(word):
		return 'Test Case 7: Success'
	return 'Failure'

def testCase8():
	word = 'hello1'
	if wordChecker.doesMeetGuidelines(word):
		return 'Failure'
	return 'Test Case 8: Success'

def testCase9():
	word = '12345'
	if wordChecker.doesMeetGuidelines(word):
		return 'Failure'
	return 'Success'

def testCase10():
	word = ''
	if wordChecker.doesMeetGuidelines(word):
		return 'Failure'
	return 'Test Case 9: Success'

def testCase11():
	word = 'ABC#'
	if wordChecker.doesMeetGuidelines(word):
		return 'Failure'
	return 'Test Case 10: Success'

def testCase12():
	word = 'A'
	if wordChecker.doesMeetGuidelines(word):
		return 'Failure'
	return 'Test Case 11: Success'

def testCase13():
	word = ' Hello123 '
	if wordChecker.doesMeetGuidelines(word):
		return 'Failure'
	return 'Test Case 12: Success'

# Add 2 test cases below:

# def myTestCase1():

# def myTestCase2():


print '*******************************************'
print testCase1()
print '*******************************************'
print testCase2()
print '*******************************************'
print testCase3()
print '*******************************************'
print testCase4()
print '*******************************************'
print testCase5()
print '*******************************************'
print testCase6()
print '*******************************************'
print testCase7()
print '*******************************************'
print testCase8()
print '*******************************************'
print testCase9()
print '*******************************************'
print testCase10()
print '*******************************************'
print testCase11()
print '*******************************************'
print testCase12()
print '*******************************************'
print testCase13()
print '*******************************************'

# Uncomment the following lines after you have written your tests 
# print myTestCase1()
# print '*******************************************'
# print myTestCase2()
#print '*******************************************'
