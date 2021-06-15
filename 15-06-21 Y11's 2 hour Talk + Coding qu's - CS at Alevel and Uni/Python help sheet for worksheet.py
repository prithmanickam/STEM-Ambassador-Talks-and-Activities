#python help sheet

#this is just for reading, don't run it

# also this is not exhausive of all the function in python, this is just so
# it helps with the worksheet

#----general-------------

'str123' #is a string
'1234'   #is a string
1234     #is a integer
1234.5   #is a float
True     #is a boolean
False    #is a boolean

#To convert a integer to a string, use str()
str(1234)    #=> '1234

#similarly to convert a string to an integer, use int()
int('1234')  #=> 1234


#python functions
if 'runs'.endswith('s'):
    print('true')
    
if 'runs'.endswith('s') and 'runs'.startswith('r'):
    print('true')

print(sum([2,3,4]))  #=> 9
print(min([2,3,4]))  #=> 2
print(max([2,3,4]))  #=> 4


#prints 4...7 on a new line
for i in range(4, 8):
    print(i)
#4
#5
#6
#7

li = ['a','b','c','d']
for i in range(len(li)):
    print(i)
#0
#1
#2
#3

for i in range(len(li)):
    print(li[i])
#a
#b
#c
#d
    

# break escapes from a loop
while True: # loop for ever
    print(x)
    x += 1 # Shorthand for x = x + 1
    if x>4:
        break # stop if x>4

# continue skips the rest of an iteration
for i in range(5):
    if i==3:
        continue # we won't print anything if i is 3
#0
#1
#2
#4

#user input
username = input("Enter username:")
print("Username is: " + username)

#import random, functions
import random

print(random.randint(0,5))
#as you keep re-running it gives a random integer between 0 and 5

li = ['a','g','l','j','f','t','v','i','w']
length = 6
string = "".join(random.sample(li,length)) #length needs to be less than length of li
print(string)
#as you keep re-running it gives a random string length 6, where all character are in li
#e.g.


#-----strings------------------------------------------------------------

# Strings are immutable.
# Strings are stored as integers internally (ASCII codes, 0 - 127).
# Strings are iterables. (you can use a for loop and iterate through each character)
                        #(similar to lists in this regard)

#to create an empty string
string = ''

# word = "hEre ArE soMe Case SensiTive woRDs 123"

print(word.lower()) # here are some case sensitive words 123
print(word.upper()) # HERE ARE SOME CASE SENSITIVE WORDS 123
print(word.capitalize()) # Here are some case sensitive words 123
print(word.title()) # Here Are Some Case Sensitive Words 123
print(word.swapcase()) # HeRE aRe SOmE cASE sENSItIVE WOrdS 123


# string operations

# split by space is default
print("some words we wish to split by space".split())
#['some', 'words', 'we', 'wish', 'to', 'split', 'by', 'space']

# split by :
print("some:words:we:wish:to:split:by:colon".split(":"))
#['some', 'words', 'we', 'wish', 'to', 'split', 'by', 'space']

# joining strings. Each element must be a string
print('*'.join(['an', 'efficient', 'way', 'of', 'concatenating', 'strings']))
# an*efficient*way*of*concatenating*strings


print("programming".index("o")) # find the position of a substring
# => 2
# (the first index is always 0)
#.index() raises error if index is not present,
#However .find() returns -1 if substring not present


string = "hypothesis"
print(string[0]) # index (first element)
#h

print(string[-1]) # index (last element)
#s

print(string[:5]) # slice
#hypot

print(string[4:-1]) # slice
#thesi

#string(start:stop:step) #the step bit is optional

print(string[:len(string):2])
#hptei

print(string + ": true") # concatenate
#hypothesis: true

print(string * 2) # repeat
#

print(len(string)) # length
#

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!") # => Hello, World!


for char in string: # iterate
    print(char, end='-')
#h-y-p-o-t-h-e-s-i-s-
    
print("h" in string) # membership

#lexicographic ordering
Aardvark<Zebra # => True
Aardvark<Aarhus # => True

#convert a character to am integer value using
ord(A) #=> 65

#convert an integer code back to a character using
chr(65) #=> A

"AAB" < "Aab"
#is equivalent to the test:
[65, 65, 66] < [65, 97, 98]


'''
space (character 32)
\n newline (character 10) print("Hi\nare\nyou\nice?") #=> Hi,are,you,ice? all newline
\r carriage return (character 13)
\t tab (character 9) print("Before tab" + chr(9) + "After tab") # => Before tab After tab 
'''

#-----lists------------------------------------------------------------

#Lists (or Arrays)
# Lists are ordered.
# Lists can contain elements of different types. e.g. c = ["string", 2, 3.0, True, {"hello": "world"}]
# List elements can be accessed by index.
# Lists can be nested to arbitrary depth.
# Lists are mutable.
# Lists are dynamic - they can grow and shrink.

list1 = ['bravo', 'charlie', 'delta', 'echo', 'fox']

#adding 'fox' to the end of the list, list1
list1.append('fox')


# remove a known element
list1.remove("fox") #removes 'fox from list1

#remove if index is known
del list1[5] #removes 'fox' from list1

# insert an element in a position
list1.insert(0, "alpha")


# extend the list with elements from another list
# also modifies in place
list1.extend(["golf", "hotel", "india"])
print(list1)
# ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'golf', 'hotel', 'india']

# iterating through element and position
for index, item in enumerate(list1):
    print(index, item)
#0 alpha
#1 bravo
#2 charlie
#3 delta
#4 echo
#...

li = [1,2,3,4]

li[-1] #=> 4

# Select every second entry
li[::2] # => [1, 4]

# Reverse a copy of the list
li[::-1] # => [4, 3, 2, 1]

li.remove(0) #=> removes the element of the index 0

li.pop(0) #=> print the element of the index 0, as well as removes the element


li2 = [5, 6]
# You can add lists
li + li2 # => [1, 2, 3, 4, 5, 6]
# Note: values for li and for other_li are not modified.

# Concatenate lists with "extend()"
li.extend(li2) # Now li is [1, 2, 3, 4, 5, 6]

# Remove first occurrence of a value
li.remove(2) # li is now [1, 3, 4, 5, 6]

# Insert an element at a specific index
li.insert(1, 2) # li is now [1, 2, 3, 4, 5, 6] again

# Get the index of the first item found
li.index(2) # => 1

# Check for existence in a list with "in"
1 in li # => True

# Finds the length with "len()"
len(li) # => 6


#Sort 
listOfStr = ["s", "m", "t", "o", "a", "l"]
listOfStr.sort() # => ['a', 'l', 'm', 'o', 's', 't']


#list comprehension (shorter way to write for loops shorter)

listOfStr = ["s", "m", "t", "o", "a", "l"]
li = []
for i in listOfStr:
    li.append(i.upper())
print(li)
#["S", "M", "T", "O", "A", "L"]

   #can be written shorter as

li = [i.upper() for i in listOfStr]
print(li)
#["S", "M", "T", "O", "A", "L"]


#Map
# map() takes two parameters: a function that has one parameter and an iterable (e.g., list, dictionary, set or
# tuple).
# Then it applies the function on each element of the iterable.

def newfunc(a):
    return a*a

x = map(newfunc, [1,2,3,4])
print(list(x))
#[1, 4, 9, 16]

# convert each integer in a list to string
nums = [1, 0, 1, 1, 1, 0]
list(map(str, nums))
['1', '0', '1', '1', '1', '0']



#-----dictionaries------------------------------------------------------------

# Dictionaries store mappings, key and value 

#create an empty dictionary
empty_dict = {}

# Here is a prefilled dictionary
dict1 = {"sam": 4, "tom": 9, "alan": 7}

dict2 = {i: i for i in range(200)}


#add a key-value pair
dict1['falkner'] = 5

# Look up values with []
filled_dict["sam"] # => 4


# Get all keys as a list with "keys()"
list(dict1.keys()) # => ["sam", "tom", "alan"]

# Your results might not match this exactly.

# Get all values as a list with "values()"
list(filled_dict.values()) # => [3, 2, 1]


# Check for existence of keys in a dictionary with "in"
# membership test using 'in', only works for key and not values
'tom' in filled_dict # => True
'harry' in filled_dict # => False

# Looking up a non-existing key is a KeyError
dict1["four"] # KeyError

# Use "get()" method to avoid the KeyError
dict1.get("sam") # => 4

dict1.get("harry") # => None



# iterating over dictionaries ----------
d = {"walking": "slow", "cycling": "medium", "driving": "fast"}

for key in d: 
    print(k, "=", d[key]) #=> walking = slow


#iterating through key, value pairs
for k,v in d.items():
    print('the key' + str(k) + 'is' + str(v))

#the key walking is slow
#the key cycling is medium
#the key driving is fast
    
d={'place1': 2, 'place2': 2, 'place3': 4}
print(list(d.items())) #returns a list of tuples
#[('place1', 2), ('place2', 2), ('place3', 4)]

#keys can only be of an immmutable type, therfore can't be lists




