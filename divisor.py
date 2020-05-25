number = int(input("What is the number that you want to check the divisor: "))

listRange = list(range(1,number + 1))

divisorList = []

for num in listRange:
	if number % num == 0:
		divisorList.append(num)

print(divisorList)
