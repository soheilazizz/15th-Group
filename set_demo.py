# set:
# unordered Data types
# you can not define empty set using literals
# mutable

emptyset = set()
newset = {1,'ali',2,'a'} #مجموعه عضو تکراری نمی پذیرد
newset1 = {1,1,'a','a','ali',2}
print(newset)
print(newset1) # عدم پذیرش عضو تکراری
print('='*40)
for i in range(10):
    print(newset) #یکبار که روی حافظه تعریف می شود یک ترتیب دارد
# COMPARE to dict:
print('='*40)

sampleDict = {'name': 'Soheil',
              'surname': 'Azizi',
              'age': 37 ,
              'City' : 'Tehran'}
print(sampleDict['name'])
print('='*40)
oddset = set(range(1,50,2))
powerset = {1,4,9,16,25,36,49}
print(oddset.intersection(powerset))
print(oddset.union(powerset))
print(len(oddset.union(powerset)))
print(oddset.intersection_update(powerset)) #intersection is done and oddset
# convert to newset as the intercetion
print(oddset)
# frozenset is immutable
frozensett = frozenset(powerset)
