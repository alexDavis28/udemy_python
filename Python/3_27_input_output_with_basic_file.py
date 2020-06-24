
myfile = open("3_27_text.txt")

#opens file

print(myfile.read())
#returns text as string

myfile.seek(0)
#resets read location
print(myfile.readlines())	#returns list of lines

#to open a file at any location, use the full file path
#eg:
#	myfile = open("C:\\Users\\8m3xl\\Documents")	always use double slashes (\\) instead of (\)
#pwd python console command returns the files directory

myfile.close()
#closes file, good to use when done

#however, better is to use a with statement
#eg:
with open("3_27_text.txt") as my_new_file:
	#you don't need to worry about closing the file, becuase it assigns the file to the variable my_new)file
	contents = my_new_file.read()


with open("3_27_text.txt",mode='r') as my_new_file:
	contents = my_new_file.read()

'''
open modes:
mode='r'	is read only
mode='w'	is write only, overwrites files or creates new ones
mode='a'	append only,adds on to files
mode='r+'	reading and writing
mode='w+'	writing and reading, overwrites exisiting files or crates a new file
default is r
'''
#NEW FILE IS 3_27_text2.txt

with open("3_27_text2.txt",mode='a') as f:
	f.write("\nFOUR ON FOURTH")
#adds text to the end of the file, with \n for a new line

with open("3_27_text3.txt",mode ='w') as f:	#becuase there is no file with that name, this would create a new one called that
	f.write("I created this file")
	#i have one this, so it will only override this file