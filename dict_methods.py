# The clear() method removes all the elements from a dictionary.
import copy
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)
# ---------------------------------------------------
# The copy() method returns a copy of the specified dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy() # methods

print(x)
y = copy.copy(x) # madule
print(y)
# ---------------------------------------------------

# The fromkeys() method returns a dictionary with the specified keys and the specified value.
# dict.fromkeys(keys, value)
print('+'*40)
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
print('+'*40)

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)
print('+'*40)

# ---------------------------------------------------
# The get() method returns the value of the item with the specified key.
# dictionary.get(keyname, value)
y = car.get('model')
print(y)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('+'*40)

# ---------------------------------------------------
# The items() method returns a view object. The view object
# contains the key-value pairs of the dictionary, as tuples in a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)

car['price'] = 15000
print(car)
print('+'*40)

# ---------------------------------------------------
# The keys() method returns a view object. The view object
# contains the keys of the dictionary, as a list.
print(car.keys())
print('+'*40)


x = car.keys()

car["color"] = "white"

print(x)
# ---------------------------------------------------
# The pop() method removes the specified item from the dictionary.
# dictionary.pop(keyname, defaultvalue)
print('+'*40)
oldcar = copy.copy(car)
car.pop("model") #>>>like list and mutable
print(oldcar)
print('+'*40)
print(car)
# ---------------------------------------------------
#The popitem() method removes the item that was last inserted into the dictionary.
print('+'*40)

oldcar.popitem()
print(oldcar)
print('+'*40)
# ---------------------------------------------------
# The setdefault() method returns the value of the item with the specified key.
y = car.setdefault('year')
print(y)
# if the "color" item does not exist, insert "toprange" with the value "lastver"
h = car.setdefault('toprange','lastver')
print(h)
print(car)
print('='*40)

# ---------------------------------------------------
# The update() method inserts the specified items to the dictionary.
# dictionary.update(iterable)
oldcar.update({'toprange':'lastver'})
print(oldcar)
# >>>another war:
print('='*40)

oldcar['stm'] = '2efr'
print(oldcar)
# ---------------------------------------------------
print('='*40)

# The values() method returns a view object.
# The view object contains the values of the dictionary, as a list.
listvalue = oldcar.values()
print(listvalue)