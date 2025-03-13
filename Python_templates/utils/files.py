


f = open("demofile.txt", "r")
print(f.read())

# Return the 5 first characters of the file:
print(f.read(5))

# Read a line
print(f.readline())

## loop through the file and print line by line
for x in f:
  print(x)

## read and write
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


f.close()