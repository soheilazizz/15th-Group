smaplestring = "ABCD"
for char in smaplestring:
    print(char)

# i : itrator
# smapletring: iterable object
char = iter(smaplestring)
samplelist = [1, 2 ,3]
elem = iter(samplelist)
print(type(char))
print(type(elem))
# تولید ایترتور به صورت دستی در شرایطی که میخواهیم نامنظم اجرا شود
print('='*40)
print(next(char))  #A
print(next(char))  #B
print(next(char))  #C
print(next(char))  #D
print(next(char))  #Eror