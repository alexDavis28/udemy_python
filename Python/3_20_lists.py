#lists support indexing and slicing and can be nested
my_list = [1,2,3]
my_second_list = ["string",100,23.2]	#can hold different data types
print(my_list[0])	#prints 1
print(my_list[1:])	#prints [2,3]
another_list = [4,5]
print(my_list+another_list)	# prints[1,2,3,4,5]

#lists are muutable
new_list = ["one","two","three","four"]
new_list[0] = "ONE ALL CAPS"

#remove from list
new_list.pop() #removes end item and returns it
nwe_list.pop(0)#removes from position 0

#sort
new_list = ["a","e,","x,","b","c"]
num_list = [4,1,8,3]
new_list.sort()
print(new_list)	#returns new_list, sorted in place, in alphabetical order 
new_list.reverse()#guess

#lists cna be placed ito other lists
list_list = [new_list, num_list]
print(list_list[1][0])	#returns first value of second list