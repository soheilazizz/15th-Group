# List VS Range
import sys
smallrange = range(10)
smalllist = list(range(10))
bigrange = range(100)
biglist = list(range(100))
print("size of smallrange : {}".format(sys.getsizeof(smallrange)))
print("size of bigrange : {}".format(sys.getsizeof(bigrange)))
print("size of smalllist : {}".format(sys.getsizeof(smalllist)))
print("size of biglist : {}".format(sys.getsizeof(biglist)))
# تابع رنج حافظه ندارد و بنابراین به اعداد قبل و بعد خود دسترسی ندارد
# تابع رنج جای کمی در حافظه اشغال می کند

# بخشپذیری
a = 124484479764692747429229
print(a in range(0,99999999999999999999999999999999999999,1401))
