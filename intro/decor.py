#  a tool to calculate the cost of painting a room

# sqft_walls = total square feet of walls to be painted
# sqft_ceiling = square feet of ceiling to be painted
# sqft_per_gallon = number of square feet that you can cover with one gallon of paint
# cost_per_gallon = cost (in dollars) of one gallon of paint

import math as m


def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):

    total_sqft = sqft_walls + sqft_ceiling  # calculate the total sqaurefeet

    # calculate the number of gallons needed
    gallons = m.ceil(total_sqft / sqft_per_gallon)

    cost = gallons * cost_per_gallon

    return cost


print(get_cost(432, 144, 400, 15))
