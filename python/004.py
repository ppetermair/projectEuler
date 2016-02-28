def isPalindromic(number):
	numberAsString = str(number)
	if numberAsString == numberAsString[::-1]:
		return True
	return False

firstMultiplier = 999
secondMultiplier = 999

palindromicNumbers = []
while firstMultiplier > 99 and secondMultiplier > 99:
	result = firstMultiplier * secondMultiplier
	if isPalindromic(result):
		palindromicNumbers.append(result)
		print "{0} * {1} is {2}".format(firstMultiplier, secondMultiplier, result)
	secondMultiplier -= 1
	if secondMultiplier == 99:
		firstMultiplier -= 1
		secondMultiplier = 999
print "max palindromic number is {0}".format(max(palindromicNumbers))