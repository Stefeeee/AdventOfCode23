import re

with open("1\input_1.1.txt", "r") as calibrationValues:
	calValuesLines = calibrationValues.readlines()

	sum = 0
	for calValue in calValuesLines:
		calValueReversed = calValue[::-1]
		firstNumber = re.search(r'\d+', calValue).group()[0]
		lastNumber =  re.search(r'\d+', calValue[::-1]).group()[0]
		valueNumberCombined = firstNumber+lastNumber
		sum = sum + int(valueNumberCombined)

	print("totalValue: ")
	print(sum)
		
