# https://www.w3schools.com/python/python_sets.asp

# Using curly braces
mySet=set()
mySet.add("one")

set1 = {"apple", "banana", "cherry"}
print("Set1:", set1)

# Using the set() constructor
set2 = set(["apple", "banana", "cherry"])
print("Set2:", set2)

# Adding a single element
set1.add("orange")
print("After adding 'orange':", set1)

# Adding multiple elements using update()
set1.update(["mango", "grape"])
print("After adding multiple elements:", set1)

# Using remove() (raises KeyError if element doesn't exist)
set1.remove("banana")
print("After removing 'banana':", set1)

# Using pop() (removes a random element as sets are unordered)
removed_item = set1.pop()
print(f"Removed item: {removed_item}, Set after pop: {set1}")

# Clearing the entire set
set1.clear()
print("After clearing the set:", set1)