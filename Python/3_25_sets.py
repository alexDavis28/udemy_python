#unorderd collections of unique elemnts
#there can only be instance of unqiue objects

myset = set()
myset.add(1)
print(myset)	#returns 1
myset.add(2)
myset.add(2)	#wouldn't work, just wouldn't add

#useful for castinga list to a set to remove duplicates

mylist = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]
print(set(mylist))# prints {1,2,3}, so only unique values