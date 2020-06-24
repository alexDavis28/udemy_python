# when using a for loop with a .append(), you can use list comprehension
mylist = [i for i in "hello"]
mylist = [num**2 for num in range(0,11)]

celcius = [0,10,20,30,34.5]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]

# if, else statements

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)
#prints ([0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10])

#nested loops
mylist = []
for x in [2,4,6]:
	for y in [100,200,300]:
		mylist.append(x*y)

#or

mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
#howver,  focus on readibilty
