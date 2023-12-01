import re

with open("input_1.1.txt", "r") as calibrationValues:
	calValuesLines = calibrationValues.readlines()

sum = 0
for calValue in calValuesLines:
    #replace with first and last to account for overlap
    if("zero" in calValue):
        calValue = calValue.replace("zero", "z0o")
    if("one" in calValue):
        calValue = calValue.replace("one", "o1e")
    if("two" in calValue):
        calValue = calValue.replace("two", "t2o")
    if("three" in calValue):
        calValue = calValue.replace("three", "t3e")
    if("four" in calValue):
        calValue = calValue.replace("four", "f4r")
    if("five" in calValue):
        calValue = calValue.replace("five", "f5e")
    if("six" in calValue):
        calValue = calValue.replace("six", "s6x")
    if("seven" in calValue):
        calValue = calValue.replace("seven", "s7n")
    if("eight" in calValue):
        calValue = calValue.replace("eight", "e8t")
    if("nine" in calValue):
        calValue = calValue.replace("nine", "n9e")
   
    calValueReversed = calValue[::-1]
    firstNumber = re.search(r'\d+', calValue).group()[0]
    lastNumber =  re.search(r'\d+', calValueReversed).group()[0]
    valueNumberCombined = firstNumber+lastNumber
    sum = sum + int(valueNumberCombined)

print("totalValue: " + str(sum))
		
