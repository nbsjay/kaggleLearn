food = ["potatoes", "rice", "fufu", "fufu", "crab", "rice", "prawns", "jollof"]

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    # iterate over the indexes of the list
    for i in range(len(meals)-1):
        # if a value is the same as the value after it
        if meals[i] == meals[i + 1]:
            # return 'True
            return True
    return False

print(menu_is_boring(food))