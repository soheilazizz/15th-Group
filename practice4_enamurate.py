samplealphabet = 'ABCDEF'
samplenumbers = '123456'
AlphabetString = 'ABCDEFGHIJKLMNOPQRSTVWXYZ'

for numb ,char in zip(samplenumbers , samplealphabet): # قسمت فرد
    if not int(numb) % 2:
        continue
    print(f'{numb}:{char}')
print('='*40)
for numb ,char in zip(samplenumbers , samplealphabet): # قسمت زوج
    if  int(numb) % 2:
        continue
    print(f'{numb}:{char}')
for ind, char in enumerate(reversed(AlphabetString),1) : #برای یک آیتم قابل شمارش انجام م یدعد انجام برعکس
    print('character #{}:{}'.format(ind,char))
    print("=" * 40)
    samplealphabet = 'ABCDEF'
    samplenumbers = '123456'
for indx , char in zip(reversed(samplenumbers),reversed(samplealphabet)) :
    print(f'{indx}:{char}')
print('='*40)
for ind, char in enumerate(AlphabetString,1) :#قسمت فرد
    if ind%2==0 :
        continue
    print('character #{}:{}'.format(ind,char))
print('='*40)
for ind, char in enumerate(AlphabetString, 1):  # قسمت زوج
    if  ind % 2 != 0 :
        continue
    print('character #{}:{}'.format(ind, char))
print('='*40)

#  پاسخ استاد << من مساله را درست نفهمیدم باید برنامه ای می نوشتم که حروف روج فرد را دو تا دو تا کنار هم بنویسه
print('='*40)
for odd , even in zip(AlphabetString[::2],AlphabetString[1::2]) :
     print(f'{odd},{even}')
print('='*40)
for odd , even in zip(reversed(AlphabetString[::2]),reversed(AlphabetString[1::2])) :
     print(f'{odd},{even}')
