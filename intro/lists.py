# list are created with [..,..] commas are used to separate values
# every item in a list is a python string so each is enclised in quotation marks

clique = ["Nathan", "James", "Jake", "Lilith",
          "Godwill", "Sarah", "August", "Lara"]

print(len(clique))  # get the number of entries in the list

# using indexes, you can retieve entries from a list.
print("the first entry in the list is ", clique[0])
# 0 here retireves the first entry

# Slicing - you can also pull a segment of a list
# pull the first three entries
print("the first three entries are  ", clique[:3])
print("the last two entries are  ", clique[-2:])  # pull the last two entries
# when you slice a list, it returns a new shortned list

# to remove an item, use .remove() method
clique.remove("Portia")
print(clique)

# to add an item, use .append() method
clique.append("John")
print(clique)


# lists can have items with any datatype - integer, boolean, float etc

sales = [43, 882, 12,  90, 714,  510, 216, 300, 620, 150]
print(len(sales))

# min() and max() can be used with number datatypes
print(min(sales), max(sales))
print(sales[:2])  # print the first two entries
print(sales[-4:])  # print the last 4 entries

print("the sum of list items is ", sum(sales))  # add every item in the list

print(len(sales))


# split() method can be used to turn a string into a list
# the separator should be spicified within quotation marks
# example - list.split(",")
