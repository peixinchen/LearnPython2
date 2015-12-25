#! /usr/bin/env python2

dishes = {
    'eggs': 2,
    'sausage':  1,
    'bacon':    1,
    'spam': 500,
}

carts = {
    'eggs': 10,
    'spam': 30,
    'potatoes': 5,
}

keys = dishes.viewkeys()
values = dishes.viewvalues()

print(keys)
print(values)

dishes['butter'] = 30

print(keys)
print(values)

del dishes['eggs']

print(keys)
print(values)

keys2 = carts.viewkeys()
values2 = carts.viewvalues()

print(keys & keys2)
print(keys | keys2)
print(keys - keys2)
print(keys ^ keys2)
