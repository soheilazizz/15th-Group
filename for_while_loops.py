# General structure:
# for <iterator> in <iterable object>
#   1)
#   2)
#   3)
#    ....

AlphabetString = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'
for char in AlphabetString :
    print(char)
print("="*40)
# classic like C
for i in range(len(AlphabetString)) :
    print(AlphabetString[i])
print('='*40)
for char in AlphabetString : # in means belonging to a set like range,..Alphabetstring , ,,,,
    if char in 'cQmnr' :
       break  #break means:>> شکسته شدن حلقه و دستور بعدانجام نمیشه
    if char in 'CFGJK':
       continue
    print(char) #continue means >> حلقه وقتی به این میرسد از روی آن می پرد

for char in AlphabetString :
    if char in 'cqmnr' :
       break
    if char in 'CFGJK':
       continue
    print(char)
else :
    print('اگر حلقه شکسته نشه من چاپ میشم')
# enumerate: What does enumerate do in Python? The enumerate function in Python converts a data collection object
# into an enumerate object. Enumerate returns an object
# that contains a counter as a key for each value within an object, making items within the collection easier to access
for ind, char in enumerate(AlphabetString,1) : #برای یک آیتم قابل شمارش انجام م یدعد
    print('character #{}:{}'.format(ind,char))
# zip: Python's zip() function creates an iterator that will aggregate elements
# from two or more iterables. You can use the resulting
# iterator to quickly and consistently solve common programming problems, like creating dictionaries
print("="*40)
samplealphabet = 'ABCDEF'
samplenumbers = '123456'
for ind , char in zip(samplenumbers,samplealphabet) :
    print(f'{ind}:{char}')
    print("=" * 40)
print("=" * 40)
# while..loop
# while <condition>
# 1)
# 2)
# ....
counter = 0
while counter < 5:
    print(f"the count is : {counter}")
    counter = counter + 1
# while (A and B) or C:
# while True:
# if A:
#  ......
#    break
# if B:
# ..........
#    break
print("=" * 40)
# input function>>> ***input is always string****
inp = input("enter a number")
print(inp)
# what is the diferent between for and while?
# when we don't know how many iteration we have we use while