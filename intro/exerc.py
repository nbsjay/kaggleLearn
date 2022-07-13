# a function that returns the percentage growth in the total number of users relative to a specified number of years ago.
# num_users = Python list with the total number of users each year. So num_users[0] is the total number of users in the first year,
# num_users[1] is the total number of users in the second year, and so on.
# yrs_ago = number of years to go back in time when calculating the growth percentage


def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users) -
              yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth


num_users_test = [920344, 1043553, 1204334, 1458996,
                  1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

print(percentage_growth(num_users_test, 1))

print(percentage_growth(num_users_test, 7))
