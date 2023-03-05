# mapping
# dictionary
emptydictionary = {}
enotheremptydic = dict()
# Dictionary : key + amount
sampleDict = {'name': 'Soheil',
              'surname': 'Azizi',
              'age': 37 ,
              'City' : 'Tehran'}
print(sampleDict['name']) # print
print(hex(id(sampleDict)))
sampleDict['education'] = 'Diploma'
print(hex(id(sampleDict)))
# Accessing values in dictionary can only through keys
# Dictionaries are mutable
# view object
print(sampleDict.keys())
keylist = list(sampleDict.keys())  # dict.keys>>>>list>>iterable
print(keylist)
#--------------------------------------
print('='*40)  # dict.values>>>>list>>iterable
valuelist = list(sampleDict.values())
print(valuelist)
#--------------------------------------
print('='*40)  # dict.item>>>>list or tuple>>
itemlist = list(sampleDict.items())
print(valuelist)
itemtuple = tuple(sampleDict.items())
print(itemtuple)

print('='*40)
#---------------------------
# make dictionary from tuple
newdict = dict(itemtuple)
print(newdict)
 # insertion oredr <<>>> memory order
# کلید دیکشنری حتما باید immutable باشد.

# somdict = {[1,2]: 3, 'has': 4} غیر قابل اجرا
print('='*40)
# search in ditionaries
for k in sampleDict:
    print(k) # keys are printing
print('='*40)
for k in sampleDict:
    print(sampleDict[k]) # values are printnig # compercity >>>O(N)
print('=' * 40)
for v in sampleDict.values():
    print(v)  # values are printnig# compercity >>>O(N^2)


