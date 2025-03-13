


"""
for loops
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


for x in range(6):
  print(x)

for x in range(2,6):
   print(x)

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)


"""
While loops 
"""

i = 1
while i < 6:
  print(i)
  i += 1

# Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)