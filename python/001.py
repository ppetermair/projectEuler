sum = 0
for number in xrange(1,1000):
	if number % 3 == 0 or number % 5 == 0:
		sum += number
print(sum)
