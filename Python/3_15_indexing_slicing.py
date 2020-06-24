'''
indexing grabs a character in a string with a specifc index
'''

mystring = "Hello world"

print(mystring[0])	#prints H
print(mystring[8])	#prints r

print(mystring[9])	#prints l
print(mystring[-2])	#prints l, negative values go bacwards from start, with the first character being 0

#slicing grabs a subsection of the string

mystring = "abcdefghijk"

print(mystring[2:]) #prints everything from the index 2, so cdefghijk

print(mystring[:3]) # prints up to index 3 but not including, so abc

print(mystring[3:6]) # prints def, index position 3 up to but not including 6

print(mystring[::])	#prints entire string, not really used

print(mystring[::2]) # prints acegik, everything in the string, witha step size of 2

print(mystring[::-1])	#reverse string