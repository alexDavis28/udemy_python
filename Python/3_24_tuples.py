#tuples are like lists, but immutable
#use parentheses
#can mix object types
#slicing and indexing work
#immutable
t = (1,1,2,3)
my_list = [1,2,3]

#2 in-built methods
t.count(1)	#returns number of times 1 appears in the tuple
t.index(2)	#returns index of 2 in the tuple

#used mainly for passing objects when you don't want them to be changed
#provides data integrity