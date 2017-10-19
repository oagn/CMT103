# CMT103 Wk1, task 1
# register.py

yName = input("What is your name? ")
print("\nHi, {name}, how do you do?".format(name=yName))

yAge = int(input("How old are you, {name}? ".format(name=yName)))

print("\nGreat, {name}, I am {age} years old too".format(name=yName, age=yAge))

yCity = input("Which city do you come from, {name}? ".format(name=yName))
print("\nWhat a coinsidence, I am from {city} too!".format(city=yCity))

print("""{name}, here is your record ...
	{NAMEt: <30} {AGEt: <5} {CITYt: <30}
	-------------------------------------------------------
	{name: <30} {age: <5} {city: <30} """.format(NAMEt="NAME", AGEt="AGE", CITYt="CITY", name=yName, age=yAge, city=yCity))