def to_smash(total_candies, nfrnds=3):

    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between friends.
    allow user to input the number of candies and friends. the default number of friends is 3
    
    >>> to_smash(91)
    1
    """
 

    return total_candies % nfrnds

friends = int(input("How many friends?  "))
candies = int(input("How many candies?  "))

smash = to_smash(candies, friends)

print("Candies to be smashed: ", smash)