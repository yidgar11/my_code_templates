# https://www.w3schools.com/python/python_dictionaries.asp

# create dictionary using { }
d=dict()
d['first'] = 1

d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)
print(d2['a'])
print(d2.get('b'))

print("\nAdding a new key-value pair - d2['age'] = 22")
d2['age'] = 22
print(d2)

print("\nUpdating an existing value - d2['age'] = 23")
d2['age'] = 23
print(d2)

print("\nUsing del to remove an item - del d2['age']")
del d2['age']
print(d2)

print("\nUsing pop() to remove an item and return the value - d2.pop('a')")
val = d2.pop('a')
print(val)

print("\nIterate over keys")
for key in d2:
    print(key)

print("\nIterate over values")
for value in d2.values():
    print(value)

print("\nIterate over key-value pairs")
for key, value in d2.items():
    print(f"{key}: {value}")