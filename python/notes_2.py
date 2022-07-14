"""
when wtiting code, pay attention to the order of operations. Use parentheses to help prevent bugs and
make the intentions of your code clearer.
"""

"""
like int() and float() which convert to their respective data types, bool() converts values to boolean
numbers are converted to 'True', '0' is converted to false, strings are converted to 'True' and and empty
string is converted to 'False'
"""

print(bool(1))
print(bool(0))
print(bool("abc"))
print(bool("")) # take care to not input a space in the quotes

"""
converting a bool with 'True" to int results to 1
converting a bool with "False" to int results to 0
"""
x = bool(1)
print(int(x))

lst = [[1, 2, 3], [3, 2, 1], [4, 5, 6]] # A list of lists

"""
lists functions, methods and Slicing
"""
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupyter", "Saturn", "Uranus", "Neptune"]

planets[0:3] # picks the first value through to the third value in the list
planets[-3:] # returns the last three planets
planets[:-3] # exclude the last three planets

planets.append("Pluto") # adds an element to a list
planets.pop() # Removes and returns the last element of a list
sorted(planets) # sort function returns a sorted version of the list
len(planets) # length function returns the length of the list
planets.index("Earth") # returns the index of earth in the list
"pluto" in planets # returns 'True' if pluto is in the list

