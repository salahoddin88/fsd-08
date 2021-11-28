""" Dict contains key value pair {key:value} """

#dict = { key : value}

student = {'name' : 'mohit', 'age': 21, "city":"Pune", "pincode":"123456"}

# how to print one value
#print(student['key])

# how to update value of key
# student[key] = "New Value"


# how to insert new key value pair
# student[NewKey] = "New Value to insert"


# copy() to copy dict into new variable
#copyStudent = student
# copyStudent = student.copy()

# print(student.keys())
# print(student.values())

#clear() make dict empty 
# student.clear()


# pop() will remove key and value from dict
# student['name'] = ''
# student.pop('name')

# nested Dict

# student = {
#     'name':'nikhil', 
#     'age' : 21, 
#     'skills' : {
#         'python' : {
#             'rating' : 6,
#             'abc' : 'abc'
#         },
#         'html' : 5,
#         'javascript' : 8,
#     }
# }
# student['skills']['python']['rating'] = 9
# print(student['skills'])