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
		print 'Test Case 1: Success'
	else:
		print "Test Case 1: Failure\nFunction: getLetterCount\nParameters: '" + word + "'"

def testCase2():
	word = "abcd"
	result = letterCount.getLetterCount(word)
	answer = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
	if equals(result, answer):
		print 'Test Case 2: Success'
	else:
		print "Test Case 2: Failure\nFunction: getLetterCount\nParameters: '" + word + "'"

def testCase3():
	word = "aaaaba"
	result = letterCount.getLetterCount(word)
	answer = {'a': 5, 'b': 1}
	if equals(result, answer):
		print 'Test Case 3: Success'
	else:
		print "Test Case 3: Failure\nFunction: getLetterCount\nParameters: '" + word + "'"

def testCase4():
	word = "1223434344"
	result = letterCount.getLetterCount(word)
	answer = {'1': 1, '2': 2, '3': 3, '4': 4}
	if equals(result, answer):
		print 'Test Case 4: Success'
	else:
		print "Test Case 4: Failure\nFunction: getLetterCount\nParameters: '" + word + "'"

def testCase5():
	word = "Hello"
	result = letterCount.getLetterCount(word)
	answer = {'H': 1, 'e': 1, 'l': 2, 'o': 1}
	if equals(result, answer):
		print 'Test Case 5: Success'
	else:
		print "Test Case 5: Failure\nFunction: getLetterCount\nParameters: '" + word + "'"

def testCase6():
	word = ""
	result = letterCount.getLetterCount(word)
	answer = {}
	if equals(result, answer):
		print 'Test Case 6: Success'
	else:
		print "Test Case 6: Failure\nFunction: getLetterCount\nParameters: '" + word + "'"

# Add 2 test cases below:

# def myTestCase1():

# def myTestCase2():


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
# print testCase7()
# print '*******************************************'
# print testCase8()
# print '*******************************************'
# print testCase9()
# print '*******************************************'
# print testCase10()
# print '*******************************************'
# print testCase11()
# print '*******************************************'
# print testCase12()
# print '*******************************************'
# print testCase13()
# print '*******************************************'

# Uncomment the following lines after you have written your tests 
# print myTestCase1()
# print '*******************************************'
# print myTestCase2()
#print '*******************************************'
