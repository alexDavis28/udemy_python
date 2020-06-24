#arguments and keyword arguments
#way to accept arbritary numebr of arguments and keyword arguments

def myfunc(a,b):
	#Returns 5% of a+b
	return (sum(a,b)) * 0.05


#a and b are positional arguments

#to work with two numbers, use *args

def myfunc(*args):
	return (sum(args)) * 0.05
#args is a tuple of all given arguments
#args can be any word, but has to have the star
#you should use args though

def myfunc(**kwargs):
	if 'fruit' in kwargs:
		print(f"My fruit of choice is {kwargs['fruit']}")

#kwargs is a dicitionary

#eg:
myfunc(fruit='apple', cheese='cheddar')
#would print 'My fruit of choice is apple'


#also

def myfunc(*args, **kwargs):
	print(f"I would like {args[0]} {kwargs['food']}")