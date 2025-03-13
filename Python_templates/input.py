__author__ = 'yidgar'
import string

## https://pyformat.info/ - general page for formatting of strings
name = input ("whats your name ? ")  ## input that will insert as a string
nameCaps = string.capwords(name) ## 1st word as caps
numberOfBrothers = input ("How many brothers you have ? ")
numberOfSisters = input ("How many sisters you have ? ")
total = numberOfBrothers + numberOfSisters

# Print - way #1
print ("Hello %s You have %s brothers and %s sisters , total: %d " % (nameCaps, numberOfBrothers,numberOfSisters, total))

# print - way #2
print ("Hello {} You have {} brothers and {} sisters , total : {}".format(nameCaps, numberOfBrothers,numberOfSisters, str(total)))
