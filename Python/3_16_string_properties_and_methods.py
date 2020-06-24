name = "sam"
#name[0] = "p"	this deosn't work because strings are immutable

last_letters = name[1:]
print("p"+last_letters)	#prints pam

#multiplication for multiple strin concatenations
letter = "z"
print(letter*10)	#prints zzzzzzzzzz

#methods

x = "Hello World"
x.upper()	#uppercases string 	HELLO World
x.lower()	#guess

x.split()	#seperates into list of words

x="Hi this is a string"
print(x.split("i"))	#splis by letter i, prints ['H', ' th', 's ', 's a str', 'ng']
