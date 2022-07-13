# Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
# Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.

# engraving - a Python string with the text of the engraving
# solid_gold - a Boolean that indicates whether the ring is solid gold

# the program should return the cost of the project


def cost_pro(engraving, solid_gold):
    cost = solid_gold * (100 + (len(engraving) * 10)) + \
        (not solid_gold) * (len(engraving) * 7 + 50)
    return cost


print(cost_pro("nbs_jay", True))

# another way to write this is with conditional statements


def cost_pro(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + (len(engraving) * 10)
    else:
        cost = 50 + len(engraving) * 7
    return cost


print(cost_pro("nbs_jay", False))
