# The capitalize() method returns a string where the first character is upper case,
# and the rest is lower case.
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)
print('='*40)

txt = "36 is my age."

x = txt.capitalize()

print (x)
print('='*40)
#-----------------------------------------------------
# The center() method will center align the string,
# using a specified character (space is default) as the fill character.
# string.center(length, character)
txt = "banana"

x = txt.center(20, "s")

print(x)
print('='*40)
#-----------------------------------------------------
# The count() method returns the number of times a specified value appears in the string.
# string.count(value, start, end)
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)
y = txt.count("apple")
print(x)
print(y)
print('='*40)
#-----------------------------------------------------
# The encode() method encodes the string, using the specified encoding.
# If no encoding is specified, UTF-8 will be used
# string.encode(encoding=encoding, errors=errors)
txt = "My name is Ståle"

x = txt.encode()

print(x)

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print('='*40)

#-----------------------------------------------------
# The endswith() method returns True if the string ends with the specified value, otherwise False.
# string.endswith(value, start, end)
# Check if position 5 to 11 ends with the phrase "my world.":

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)
print('='*40)
#-----------------------------------------------------

# The format() method returns the formatted string.
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)
print('='*40)

#-----------------------------------------------------------
# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method,
# the only difference is that the find() method returns -1
# if the value is not found. (See example below)
txt = "Hello, welcome to my world."

x = txt.index("t")
y = txt.index("m")
z = txt.find('a')
print(x)
print(y)
print(z)
print('='*40)

#-----------------------------------------------------------
# isalnum()	Returns True if all characters in the string are alphanumeric
# method returns True if all the characters are alphanumeric,
# meaning alphabet letter (a-z) and numbers (0-9).
txt = "Company12"

x = txt.isalnum()

print(x)
print('='*40)

# isalpha()	Returns True if all characters in the string are in the alphabet
x = txt.isalpha()

print(x)
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print('='*40)

print(a.isdecimal())
print(b.isdecimal())
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9),
# or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.
print('='*40)

a = "MyFolder"  # true
b = "Demo002"   #true
c = "2bring"    #false
d = "my demo"    # false

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
print('='*40)


# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# Example of none printable character can be carriage return and line feed.
txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)
print('='*40)

# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# The istitle() method returns True if all words in a text start with a upper case letter,
# AND the rest of the word are lower case letters, otherwise False.
# isupper()	Returns True if all characters in the string are upper case
####################################################################################
# ***********IMPORTANT**********************
# The join() method takes all items in an iterable and joins them into one string.
#
# A string must be specified as the separator.
myTuple = ("John", "Peter", "Vicky")
x = ",".join(myTuple)
print(x)
print('='*40)

myList = ['reza', '33', 'kooo']
x = '.'.join(myList)
print(x)
#---------------------------------------------------------------------------------------
# The ljust() method will left align the string,
# using a specified character (space is default) as the fill character.
txt = "banana"

x = txt.ljust(20, "O")

print(x)
#---------------------------------------------------------------------------------------
# The lower() method returns a string where all characters are lower case.
#---------------------------------------------------------------------------------------
# The lstrip() method removes any leading characters (space is the default leading character to remove)
print('='*40)

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)
print('='*40)

#--------------------------------------------------------------------------------------
#The maketrans() method returns
# a mapping table that can be used with the translate() method to replace specified characters.
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))
#--------------------------------------------------------------------------------------
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# The first element contains the part before the specified string.
#
# The second element contains the specified string.
#
# The third element contains the part after the string..

txt = "I could eat bananas all day"

x = txt.partition("eat")

print(x)
#--------------------------------------------------------------------------------------
# The replace() method replaces a specified phrase with another specified phrase.
# string.replace(oldvalue, newvalue, count)
#count	Optional. A number specifying
# how many occurrences of the old value you want to replace. Default is all occurrences
print('='*40)

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three",1)#>>فقط یکبار جایگزین میکند

print(x)
#--------------------------------------------------------------------------------------
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)
print('='*40)

#--------------------------------------------------------------------------------------

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")
#--------------------------------------------------------------------------------------
print('='*40)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)
print('='*40)
#--------------------------------------------------------------------------------------
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)
print('='*40)
#--------------------------------------------------------------------------------------
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)
#--------------------------------------------------------------------------------------

# Split a string into a list where each line is a list item:
print('='*40)
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

print('='*40)
#--------------------------------------------------------------------------------------

# Check if the string starts with "Hello":

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
#--------------------------------------------------------------------------------------
print('='*40)

#The strip() method removes any leading (spaces at the beginning) and trailing
# (spaces at the end) characters (space is the default leading character to remove)
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)
#--------------------------------------------------------------------------------------
# The zfill() method adds zeros (0) at the beginning of the string, until
# it reaches the specified length.
txt = "50"

x = txt.zfill(10)

print(x)