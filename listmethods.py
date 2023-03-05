# The append() method appends an element to the end of the list.

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)
print("=" * 40)
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
print(len(a))
# The clear() method removes all the elements from a list.

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print("=" * 40)
print(fruits)

# The copy() method returns a copy of the specified list.

fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
print("=" * 40)
print(x)

# The count() method returns the number of elements with the specified value.
# Return the number of times the value ... appears int the list
fruits = ['apple', ['banana', 456], 'cherry']
x = fruits.count("cherry")
print("=" * 40)
print(x)
print(type(x))
print("=" * 40)
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# The extend() method adds the specified list elements # اگر بخواهیم در یک لیست جدید قرار دهد چه کنیم؟
# (or any iterable) to the end of the current list.
print("=" * 40)
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
print("=" * 40)
# The index() method returns the position at the first occurrence of the specified value.

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)
print(type(x))

# list.insert(pos, elmnt) : nserts the specified value at the specified position.
print("=" * 40)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
print("=" * 40)
fruits = ['apple', 'banana', 'cherry']
fruits.insert(0, "orange")
print(fruits)
print("=" * 40)

# The pop() method removes the element at the specified position.

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
print("=" * 40)
x = fruits.pop(1)
print(x)
print(type(x))
print("=" * 40)

# The remove() method removes the first occurrence of the element with the specified value.

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
print(type(fruits))

# The reverse() method reverses the sorting order of the elements.

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print("=" * 40)
print(fruits)

# The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print("=" * 40)
print(cars)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print("=" * 40)
print(cars)


def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW'] # سورت بر اساس طول رشته
cars.sort(key=myFunc)
print("=" * 40)
print(cars)

print("=" * 40)
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW'] # سورت بر اساس طول رشته( از بیشترین به کمترین)
cars.sort(reverse=True, key=myFunc)
print(cars)

print("=" * 40)
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)