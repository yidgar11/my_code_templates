# https://www.w3schools.com/python/python_lists.asp

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Insert in position 1 :
thislist.insert(1, "orange")

# Append to the end
thislist.append("pear")

# Print the length
print(len(thislist))

# Print the type
print(type(thislist))

# access specifiv item
print(thislist[1])
print(thislist[2:5])

# Itteration
for x in thislist:
  print(x)

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# A short hand for loop that will print all items in a list:
[print(x) for x in thislist]
