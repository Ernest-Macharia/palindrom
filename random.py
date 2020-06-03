import random

numlist = []
list_length = random.randint(5,20)

while len(numlist) < list_length:
	numlist.append(random.randint(1,80))

list_even = [num for num in numlist if num % 2 == 0]
print(numlist)
print(list_even)