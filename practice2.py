AlphabetString = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'

for i in range(len(AlphabetString)) :
    print(AlphabetString[-i-1])


print('=' * 40)
print(AlphabetString[::-1])



print('='*40)
for char in AlphabetString[::-1]:
    print(char)