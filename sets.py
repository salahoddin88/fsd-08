""" Sets -> Duplicates are not allowed 
    {}
"""

fruits = {"Apple", "Banana", "Oranges"}
# print(fruits)
fruitsSet2 = {"Apple", "Cherry", "Smart Phone"}
# add item to a set
# fruits.add("Cherry")

# clear() remove all the items from a set
# print(fruits)
# fruits.clear()

# copy() return a copy of set
# fruitsCopy = fruits
# fruitsCopy = fruits.copy()
# print(fruitsCopy)

# difference() return a difference between provided sets
# differece = fruitsSet2.difference(fruits)
# print(differece)

# differece () Not working as per expectation 
# fruits.difference_update(fruitsSet2)
# print(fruits)
# print(fruitsSet2)
# print(fruits)
# fruits.intersection_update(fruitsSet2)
# print(fruits)
# print(fruitsSet2)



# discard() remove the specified value from the set
# fruits.discard("Apple")

# intersection() return a set that contains the items that exist in both set
# x = intersectionSet = fruits.intersection(fruitsSet2)
# x = intersectionSet = fruits.intersection_update(fruitsSet2)


# pop() remove a random item from the set
# fruits.pop()

# remove() remove the specified item from the set
# fruits.remove("Banana")

# update() Insert the item from set 1 into set 2
# fruits.update(fruitsSet2)

# union() Returns a set that contains all items from both set and exclude duplicate items
print(fruits)
fruitsSet3 = fruits.union(fruitsSet2)
print(fruitsSet3)
