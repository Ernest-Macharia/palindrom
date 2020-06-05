import time
birthdays = {
	"Mushori": "1996/6/26",
	"kaniagu": "1994/7/03",
	"Nzale": "1989/2/16"
}

print("Welcome, we have birthdays to: ")
time.sleep(1)
for x in birthdays:
	print(x)
	time.sleep(0.7)
choice = input("Whose birthday do you want to choose? ")
if choice in birthdays:
	print("The birthday of {} is: ".format(choice))
	print(birthdays[choice])