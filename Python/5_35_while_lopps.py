x=0

while x<5:
	print(f"The current value of x is {x}")
	x+=1
else:
	print("x is 5")

#can use else statements with while loops

#loop keywords:
'''
break: breaks out of loop
continue: goes to the top of the current enclosing loop, ignoring the current value
pass: does nothing at all, placeholder
'''

#eg:

x=[1,2,3]
for item in x:
	pass

mystring = "sammy"
for letter in mystring:
	if letter ="a":
		continue
	print(letter)


mystring = "sammy"
for letter in mystring:
	if letter ="a":
		break
	print(letter)