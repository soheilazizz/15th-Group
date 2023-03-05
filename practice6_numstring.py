numberstring = '112,124,0.23,12345,1345667,.5678,-.12,-12345'
i = 0
for ind, char in enumerate(numberstring):
    if char == ',':
        i = ind - i
        print(f'{i},{ind}')
        print(numberstring[i:ind-1:])
        print('='*40)

print(len(numberstring))
pri






