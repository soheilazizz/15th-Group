AlphabetString = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'

#Indexing


print(AlphabetString[0])
print(AlphabetString[12])

#Slicing

print(AlphabetString[0 : 13])
print(AlphabetString[0 : 13 : 2])
# print(AlphabetString[start : stop : step])
print('=' * 40)
print(AlphabetString[2 : 20 : 3])
print('=' * 40)
print(AlphabetString[ : 13])
print(AlphabetString[3:])
print('=' * 40)
print(AlphabetString[-1])
print(AlphabetString[-13])
print('=' * 40)
print(AlphabetString[-1 : -10])
print(AlphabetString[0 : -10])
print(AlphabetString[ : -10])
#علت چاپ نشدن این است که دیفالت step مثبت یک است و باید در این حالت چوم جهت حرکت رو به جلوست ، استپ را منفی بگیریم
print('Dycheh')
print('=' * 40)
# AlphabetString = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'

print(AlphabetString[-1 : -10 : -2])
print('=' * 40)
#IMPORTANT
print(AlphabetString[3 : -5])
print(AlphabetString[-5 : 2 : -1])

