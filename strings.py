"""
    Strings
"""


stringOne = "This is String One"
stringTwo = "This is string Two"
stringThrid = "This is Third String"
stringForth = "This is fourth string"
stringFive = "This is fifth string"
space = " "
# result = stringOne + " " + stringTwo  # Conatinate String
# result = stringOne + space + stringTwo + space + stringThrid + space + stringForth + space + stringFive
result = f'I am a Developer {stringTwo} {stringThrid} I am a full stack developer {stringFive}'
# result = "I am a Developer " + stringTwo + " " + stringThrid + " I am a full stack developer " + stringFive
# print(result)

firstName = "Amol this first Name"
lastName = "Mundhe this is last Name"

name = f'{firstName} {lastName}'
# print('Orignal String :', name)

capsResult = name.capitalize()
# print('caps string: ' ,capsResult)

upperResult = name.upper()
# print('Upper String: ', upperResult)

lowerResult = name.lower()
# print('Lower String', lowerResult)

titleResult = name.title()
# print('Title :', titleResult)

lengthResult = len(name)
# print('length:', lengthResult)

sampleString = "my name is {name} and I am {work}"
# print(sampleString.format(name="jayesh", work="Developer"))
# print(sampleString.format(name="Amol", work="Developer"))
# print(sampleString.format(name="Mohit", work="Developer"))


stringOne = "Hello"
intOne = 2
typeCasetIntOne = str(2)
print(stringOne + str(intOne))