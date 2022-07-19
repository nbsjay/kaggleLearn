# swap first and last positions in a list

def swap(r):
    """
    Given a list of racers, replace the first placed racer with the last
    and vice versa.

    >>> list_of _racers = ["a", "b", "c", "d]
    >>> x = swap(list_of_racers)
    >>> print(x)
    >>> ["d", "b", "c", "a"]
    """
    
    r_temp = r[0] # create a temporarry list
    r[0] = r[-1]
    r[-1] = r_temp
    return r

racers = ["Carlton", "Joe", "Theophilus", "Michael", "Oscar", "Kofi", "Junior" ]

print(swap(racers))
