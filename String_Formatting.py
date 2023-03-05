AlphabetString = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'
name = 'Arash'
age = 18
print('My name is Arash , I am 18')
print('=' * 40)
print('My name is', name, ', I am', age)  # This Code is true, but it is not Pythonic
print('=' * 40)
print('my name is {} , I am {}'.format(name, age))  # This code is pythonic
print('my name is {1} , I am {0}'.format(age, name))

# >>>>>>String literals inside triple quotes, """ or ''', can span multiple
# lines of text. Python strings are "immutable" which means they cannot be
# changed after they are created
print('=' * 40)
import math

print(""" farvardin:{2}
Ordibehesht:{2}
Khordad:{2}
Tir:{2}
Mordad:{2}
Shahrivar:{2}
Mehr:{1}
Aban:{1}
Azar:{1}
Day:{1}
Bahman:{1}
Esfand:{0}""".format(29, 30, 31))

print('=' * 40)
for number in range(16):
    print('{} to power of 2 is {}'.format(number, number ** 2))
# for space >>> {:space}
print('=' * 40)

for number in range(16):
    print('{:3} to power of 2 is {:5}'.format(number, number ** 2))
# for right > and for left <
print('=' * 40)
for number in range(16):
    print('{:<3} to power of 2 is {:>5}'.format(number, number ** 2))
print('=' * 40)
for number in range(16):
    print('{:<3} to power of 2 is {:>5}'.format(number, number ** 2 / 3))
# for rounding >>>> {:.2F}
print('=' * 40)
for number in range(16):
    print('{:<3} to power of 2 is {:>5.2f}'.format(number, number ** 2 / 3))
# Casting : Converting One data type to Another
print('=' * 40)

print(float('{:.3f}'.format(math.pi)))

# Casting:  Implicit(>>python), Explicit (>>User) : Explicit is Better than Implicit
# Another Unpythonic way to print:
print('=' * 40)

print('my name is %s, I am %s' % (name, age))

# Another pythonic way to print:
print('=' * 40)

print('=' * 40)

print(f'my name is {name} , I am {age}')
print('=' * 40)

print(f'my name is {name} , I am {age}')
# Scape Characters
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is
# surrounded by double quotes:
# Code	Result	Try it
# \'	Single Quote
# \\	Backslash>>> to address my files in windows
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value
print('=' * 40)

print(f'my name is {name} \n I am {age}')