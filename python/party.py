
def f_late(arrivals, name):
    """
    Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    A guest is considered 'fashionably late' if they arrived after at least half of the party's guests.
    However, they must not be the very last guest.
    this function takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.
    """
    position = arrivals.index(name) # gets the inde of the person
    return position >= len(arrivals) / 2 and  position != len(arrivals) - 1

guests = ["Steve", "Natasha", "Thor", "Banner", "Tony", "Clint", "Wanda", "T'Challa", "Peter", "Scott"]

x = f_late(guests, input("name:   ").title())

if x == False:
    print("Early")
else:
    print("Fashionably late")