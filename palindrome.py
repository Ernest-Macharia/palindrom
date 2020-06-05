def reverse(word):
	x = ""
	for m in range(len(word)):
		x += word[len(word)-1-m]
		return x
word = input("Give out a word: \n")
x = reverse(word)
if x == word:
	print("This is a palindrome")
else:
	print("This is not a palindrome")