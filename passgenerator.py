import string
import random

def pw_generate(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_generate(int(input("How many characters are in your password? "))))
