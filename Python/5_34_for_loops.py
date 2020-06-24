'''
Iterable objects:
list
strings
dictioanrys
'''

mylist=[1,2,3,4,5,6,7,8,9,10]
for num in mylist:
	print(num)


for num in mylist:
	if num%2 == 0:
		print(num)
	else:
		print(f"Odd number: {num}")

for letter in "Hello World":
	print(letter)


for _ in "Hello World":
	print("Letter")
# _ is a palceholder when you don't want to use a variable name

my_tuple_list = [(1,2),(3,4),(5,6),(7,8)]
for item in my_tuple_list:
	print(item)
	'''
prints :
(1, 2)
(3, 4)
(5, 6)
(7, 8)
	'''

#alternativley:
for a,b in my_tuple_list:
	print(a)
	print(b)
# duplicates structure of items in the list 

#for dictionarys:
#remeber that dictionarys are not sorted

d = {'k1':1,'k2':2,'k3':3}

for item in d:
	print(item)
	#prints only the keys

for key,value in d.items():
	print(value)
	#prints values