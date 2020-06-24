#string interpolation is injecting variables into strings

#.format

print("this is a string {}".format("INSERTED"))	#prints this is a string INSERTED

print("The {} {} {}".format('fox','brown','quick'))	#prints the fox brown quick

print("The {2} {1} {0}".format('fox','brown','quick'))	#prints the quick brown fox

print("The {0} {0} {0}".format('fox','brown','quick'))	#prints the fox fox fox

print("The {q} {b} {f}".format(f="fox",b="brown",q="quick"))	#prints the quick brown fox

#float formatting
result =100/777

print("The result was {r:1.3f}".format(r=result))	#prints 0.129

#float formatting is "{value:width.precision f}"


#fstrings
name= "jose"
print(f"Hello, his name is {name}")