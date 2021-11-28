"""  
    Lambda Function: function written in 1 line using lambda keyword
    accept any number of arguments, but only has one expression

    lambda parameters : expression
"""
# def double(x):
#     return x * 2

# print(double(5))

# double = lambda x : x * 2
# multiply = lambda x, y : x * y
# fullName = lambda firstName, lastName : firstName +" "+ lastName
# ageCheck = lambda age: True if age >= 18 else False
# print(double(5))
# print(multiply(5,10))
# print(fullName("salahuddin", "Shaikh"))
# print(ageCheck(18))


""" map() = applies a function to each item in an iterable (list, tuple, etc.)
    map(function, iterable)
"""

# store = [
#     ("Shoes", 150),
#     ("Watch", 90),
#     ("Jacket", 180)
# ]

# toRupyee = lambda storeData : (storeData[0], storeData[1] * 72)

# x = list(map(toRupyee, store))
# print(x)



"""
    filter() = create a collection of elements form an iterable for which a function return True
    filter(function, iterable)
"""

# friends = [
#     ("Bulu", 12),
#     ("Nikhil", 18),
#     ("Sanjana", 19)
# ]

# age = lambda friendsData : friendsData[1] >= 20
# rollerCosterRide = list(filter(age, friends))
# print(rollerCosterRide)