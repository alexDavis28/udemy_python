#these didn't really fit into any other lecture, so are here

#range function

mylist = [1,2,3]
for num in range(10):
	print(num)
	#prints every number from 0 to 10
for num in range(3,10):
	print(num)
	#prints every number from 0 to 9, not including 10

for num in range(0,10,2):
	print(num)
	#prints every number from 0 to 9, not including 10, with a step size of 2

# range is a generator, so you have to cast it to a list to see it as a list, egL
print(list(range(0,10,2)))



#enumerate function

word="abcde"
for item in enumerate(word):
	print(item)
	# prints every item with the index position as a tuple
	# eg: (0,"a")

for index,letter in enumerate(word):
	print(index)
	print(letter)
	print('\n')
	# uses tuple unpacking


#zip function
#zipps together 2 or more lists, is generator
mylist1 = [1,2,3]
mylist2 = ["a","b","c"]
for item in zip(mylist1,mylist2):
	print(item)
	# prints tuple of the matching items at the same index positions, eg:
	#(1, "a")
mylist3 = [100,200,300,400]
for item in zip(mylist1,mylist2,mylist3):
	print(item)
	# prints tuple of the matching items at the same index positions, eg:
	#(1, "a", 100)
	#400 is not included, only zips as far as the shortest list

# to get the list:
print(list(zip(mylist1,mylist2,mylist3)))


#in operator
#checks if value in an iterable object types

if 100 in mylist3:
	print("true")
	#prints true, see line 45


#mathemeatical functions

#min,max functions
mylist = [10,20,30,40,100]
print(min(mylist))	#prints 10
print(max(mylist))	#prints 100

#random library
from random import shuffle
shuffle(mylist)
#randomly shuffles the list inplace
print(mylist)

from random import randint
#random int
print(randint(0,100))


#user input
#always accepts as a string
print(input("input"))
