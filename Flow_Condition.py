# Flow Conditions:
# if ,  elif,   else------>>>> Conditionals
# for , else ------>>>>>Loops
# While
# Classic:
# if <condition>
#     1)
#     2)
#     3)
# linter :Linting in Python checks source code as it's written and flags errors along the way —
# before we run the code
# You can also embed Pylint into editors to view the linting in real time
# chained conditioning: اول شرط اول بعد شرط دوم بعد شرط سوم
age = 13
if age > 18:   # bool(age>18)  # this is classic if
    print("to be sene ghanoni ray dadan residi")
elif 15 < age <= 18:
    print("miresi yeki do sal dige!")
elif 12 < age and age <= 15:
    print("felan sabr kon!")
else:
    print("hanooz narsidi!")
# چند نکته 1) پایتون شرطها را به ترتیب اجرا می کند 2) اولویت شرط بر اساس شرطی باشد که از نظر من مهمتر است.
#..................Unchainde: همه شرطها با هم چک م یشود
print("="*40)
age = 18
if age > 18:   # bool(age>18)  # this is classic if
    print("to be sene ghanoni ray dadan residi")
if 15 < age <= 18:
    print("miresi yeki do sal dige!")
if 12 < age <= 15:
    print("felan sabr kon!")
else:
    print("hanooz narsidi!")
# Logical False in Python:
# int : 0
# float: 0.0
# string: '' ""   """""""
# list:  []
# tuple : ()
# dictionary : {}
# set: set()
# false

if age: # boolian(age)   check if age is logical true or false
    print("we are inside condition")
if age-18:
    print(" we are out of condition")

# ternary operator
vote =True  if age>=18 else False
print('=',*40)
print(vote)

