def name_of_function(name):
	'''
	explanation docstring, shows up in help()
	INPUT: name to print
	'''
	print("hello "+name)

name_of_function("Alex")


#default argument for function:

def say_hello(name='default'):
	print("hello "+ name)


#logical arguments

#check if 'dog' in a string

def dog_check(string):
	if 'dog' in string.lower():
		return True
	else:
		return False

#or

def dog_check(string):
	return 'dog' in string.lower()

#pig latin

def pig_latin(word):
	first_letter = word[0]

	#check if vowel
	if first_letter in 'aeiou':
		pig_word = word+'ay'
	else:
		pig_word = word[1:] + first_letter + 'ay'

	return pig_word