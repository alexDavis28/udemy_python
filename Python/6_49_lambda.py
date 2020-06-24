#map function
def square(a):
	return a**2


mynums = [1,2,3,4,5, 6]



print([i for i in list(map(square, mynums))])


#needs more notes, am tired

# filter(func,list)

#func is a function that returns a boolean
#guess what list is

#the function iterates over very value in the list and returns a filter object containing every item in the lsit that satiisifed the function

#eg:

def isEven(a):
	return a%2==0


print(list(filter(isEven, mynums)))
#would print very even value in mynums
# or, using lambdas:


print(list(filter(lambda x: x%2==0, mynums)))
