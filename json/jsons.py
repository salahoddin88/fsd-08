"""
    JSON: JavaScript Object Notation
    its a string with key and value pair
"""

import json 

# test_json = '{ "name": "nikhil", "age": "28", "city": "Mumbai", "skills": "python" }'
# jsonResponse = json.loads(test_json)
# print(jsonResponse['name'])
# print(jsonResponse['age'])


carDict = (1,2,3,4,5,6)
jsonResponse = json.dumps(carDict)
print(carDict)
print(jsonResponse)

print(type(json.loads(jsonResponse)))