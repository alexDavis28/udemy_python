#dictionaries are undorded mappings for storing objects
#dictionaries use a key-value pairing
#this lets users grab objects without knowing the index location
#cannot be sorted
#syntax:
#	{"key1":"value1","key2":"value2"}

my_dict = {"key1":"value1","key2":"value2"}
print(my_dict["key1"]) #returns value1
# can uses any data type as values, even lists or dictionarys, stack index or key calls, like with nested lists, use 3_20_lists.py for reference

#to add
my_dict["key3":"value3"]

#methods

print(my_dict.keys)#prints all keys
print(my_dict.values)#prints all values
print(my_dict.items)#prints pairings