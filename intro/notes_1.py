# Negative floats are always rounded UP to the closest integer (for instance, both -1.1 and -1.9 are rounded up to -1).
# Positive floats are always rounded DOWN to the closest integer (for instance, 2.1 and 2.9 are rounded down to 2).

print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))


# When you multiply an integer or float by a boolean with value True, it just returns that same integer or float (and is equivalent to multiplying by 1).
# If you multiply an integer or float by a boolean with value False, it always returns 0. This is true for both positive and negative numbers.
# If you multiply a string by a boolean with value True, it just returns that same string. And if you multiply a string by a boolean with value False,
# it returns an empty string (or a string with length zero).

print(3 * True) # results in 3
print(-3.1 * True) # results in -3.1
print("abc" * True) # resuts in abc
print(len("abc" * False)) # results in an empty string

print(type("abc" * True))

# a ** b means a exponent b 
# a // b returns the quotient of a/b, removing the remainders
# a % b returns the modulus of a/b
# -a returns the negation of a
# 
