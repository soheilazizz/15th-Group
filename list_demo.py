# list
# Sequence: 1)Ordered 2)Index-able
# mutable
emptylist = [] # Literal: کاراکترهایی برای تعریف دیتا تایپ، اما همه دیتا تایپها لیترال ندارند.
anotherEmptylist = list() # Constructor توابع ایجاد دیتا تایپ که برای همه دیتا تایپها موجود است..
samplelist=[1,'a',3.6,4] #طول لیست در پایتون نامحدود است و انواع دیتا تایپ رامی توان در /ان قرار داد

samplestring='ABCD'
Alphabetlist = list(samplestring)
print(Alphabetlist)

# در استفاده از لیست بهتر است کل آیتم ها از یک توع داده باشد که متدها اجرا شوند مثل sort
samplelist=[1,5,3.6,4]
print(samplelist.sort()) # هیچی برنمیگردونه!!!None=nothing
# All variables in python are pointer
# List is a mutable object #بدون اینکه آدرس متغیر عوض شود اجازه تغییر دارد مثل لیست=mutable
# Immutable آدرس غوض می شود مثل نوع داده numeric
# what is pointer???
a = 5
print(hex(id(a))) # address
print("="*40)
b = 5
print(hex(id(b)))
a = a + 1
print(a,b)
print(hex(id(a))) # آدرس عوض می شود.

print('-------------------')
print(hex(id(samplelist)))
samplelist.append(20)
print(hex(id(samplelist)))# آدرس عوض نمی شود.
# using method>>>copy to define new list
print("="*40)
odd = list(range(1,20,2))
print(odd)
backup = odd.copy()
odd.append(21)
print("="*40)
print(odd)
print(backup)
print(hex(id(odd)))
print(hex(id(backup)))

# using Constructor to define new list
print("="*40)
odd = list(range(1,20,2))
backup = list(odd)
odd.append(21)
print(backup)
print(odd)
print(hex(id(odd)))
print(hex(id(backup)))

# using module>>> copy to define new list
import copy
odd = list(range(1,20,2))
backup = copy.copy(odd)
odd.append(101)
print(odd)
print(backup)
#-------------------------------------

print("="*40)
mynewlist = [2,4,7,3,[10,12,13]]
# shallow copy

back = mynewlist.copy()
back2 = list(mynewlist)
back3 = copy.copy(mynewlist)
#---------------------------
# deep copy
fulback = copy.deepcopy(mynewlist)
#---------------------------
mynewlist[-1].append(15)
mynewlist.append(101)
print('mynewlist:',mynewlist)
print('back',back)
print('back2',back2)
print('back3',back3)

# وقتی یک میتوبل داخل یکی دیگه هست آدرس داخلی مستقل هست بنابراین تغییرات روی آن اعمال می شود.
# Solution >>madule deepcopy
print("="*40)

print('fullback',fulback)

# اضاقه کردن عنصر به لیست با Operators
# 1) Normal assignment
mynewlist = [2,4,7,3,[10,12,13]]
backUp = mynewlist
mynewlist = mynewlist + [101]   # normal assinment
print('normal assinmentL:',backUp)
print('mynewlist:',mynewlist)
# 2) Augment Assinnment
print('='*40)
mynewlist = [2,4,7,3,[10,12,13]]
backUp = mynewlist
mynewlist +=[101]   # augment assinment : if a member is mutable 100% ,
# python will not change the address
print('augment assinmentL:',backUp)
print('mynewlist:',mynewlist)
