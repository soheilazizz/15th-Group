# Sequence

# immutable با تغییرات جای آنها در حافظه تغییر می کند

emptytuple = ()
anotheremptytuple = tuple()
sampletuple = 1,2,3,[2,1] # هرگونه انواع داده بهتر است در تاپل وارد شود
print(sampletuple)
print(type(sampletuple))
print(1,2,3)
print((1,2,3))
print(hex(id(sampletuple)))
# sampletuple[0] = 10 >> this is mistake because tupes do not support assignment like lists
sampletuple = sampletuple[0],10,sampletuple[2]
print(sampletuple)
print(hex(id(sampletuple)))
#-------------------------
print("="*40)
album = 'Homayoun Shajarian' , 2003 , ('Nasim_e_Vasl' , 'Sokoot' , 'Havay_e_Geryeh')
artist , year , tracks = album  # tuple unpacking
print(artist)
print(year)
print(tracks)
#-----------------------------------------
# tuple VS List
# 1) Space of memory
print("="*40)
oddlist = list(range(1,20,2))
oddtuple = tuple(range(1,20,2))
import sys
import os # for directory opration madule
print('size of memory for odd list is : {} Byte'.format(sys.getsizeof(oddlist)))
print('size of memory for odd tuple is : {} Byte'.format(sys.getsizeof(oddtuple)))
# برای وقتی که می خواهیم تغییرات زیادی در تغیر دهیم بهتر است تاپل تعریف کنیم چون جای کمتری می گیرد
# 2) records for databased :بطور پیش فرض روی تاپل قرار می گیرد هم جای کمتر هم فقط وقتی تغییر می کند که ما بخواهیم
