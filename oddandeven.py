number = int(input("Enter a number: "))
check = int(input("Enter a number to divide by: "))

if number % 4 == 0:
	print(number, "This number is a multiple of 4")
elif number % 2 == 0:
	print(number, "This number is even")
else:
	print(number, "This number is odd")

if number % check == 0:
	print(number, "is divisible by ",check)
else:
	print(number, "is not divisible by ", check)