def kmi(weight, height):
    if not (30 <= weight <= 200 and 1.0 <= height <= 3.0):
        raise ValueError("Invalid data!")

    return round(weight / (height ** 2), 1)




# def kmi(weight, height):
#     assert 30 <= weight <= 200 and 1.0 <= height <= 3.0, "Invalid data!"
#
#     return round(weight / (height ** 2), 1)