fibonacciList = [1, 2]
evenSum = 2
while True:
	nextFibonacci = fibonacciList[-1] + fibonacciList[-2];
	if nextFibonacci % 2 == 0:
		evenSum += nextFibonacci
	elif nextFibonacci > 4000000:
		break
	fibonacciList.append(nextFibonacci)
print(fibonacciList)
print(evenSum)