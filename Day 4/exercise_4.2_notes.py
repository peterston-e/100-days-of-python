# rand.choice() documentation https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

# convert string to a list https://www.askpython.com/python/string/convert-string-to-list-in-python

# convert string to a list
#given string
string1="Python is great"
 
#printing the string
print("Actual String: ",string1) 
   
#gives us the type of string1
print("Type of string: ",type(string1))  
 
print("String converted to list :",string1.split()) 
#prints the list given by split()

#given string
string2="AskPython"
 
#printing the string
print("Actual String: ",string2)
#confirming the type()
print("Type of string: ",type(string2))
 
#type-casting the string into list using list()
print("String converted to list :\n",list(string2))

#Given string
string1="This is Python"
 
print("The actual string:",string1)
 
#converting string1 into a list of strings
string1=string1.split()
 
#applying list method to the individual elements of the list string1
list1=list(map(list,string1))
 
#printing the resultant list of lists
print("Converted to list of character list :\n",list1)

#given string
string1="abc,def,ghi"
print("Actual CSV String: ",string1)
print("Type of string: ",type(string1))
 
#spliting string1 into list with ',' as the parameter
print("CSV converted to list :",string1.split(','))