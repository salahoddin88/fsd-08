""" functions are block of code """

""" built in functions """
# list = [1, 2, 3, 4, 5, 6]
# print(len(list))


# sums = sum((1, 2, 3, 4, 5,6, 90))
# print(sums)

""" User defin function """

# print("function start")
# def functionName():
#     print("This is a function")

# print("function end")
# functionName()
# print("call end")


# x = 0
# def averageFunction(num1, num2):
#     average = (num1 + num2) / 2
#     return average



# def add5InAvegrage(numAverage):
#     sums = numAverage + 5
#     print(sums)


# average = averageFunction(10, 20)
# add5InAvegrage(average)


# def greeting(name):
#     print(f"hello {name}")


# greeting(1)


""" list as an argument """

# def lists(list=[], a=0):
#     print(list)
#     print(a)
#     # print(list)
#     # print(a)
#     # print(string)
#     # print(string2)

# lists([0,0,0,1], 10)


# def addition(num1, num2, num3):
#     return (num1 - num2 ) + num3

# x = addition(num2=10, num1=20, num3=20)
# print(x)


# *args =  parameter that will pack all arguments into a tuple

# def average(*num):
#     for i in num:
#         print(i)
#     x =  sum(num) / len(num)
#     print(x)

# average(50,100)


# **kwargs = parameter that will pack all the argument into dictionary

# def hello(**values):
    
#     print("Hello", end=" ")
#     for key, value in values.items():
#         print(value, end=" ")
#     # print(f'Hello {firstName} {lastName}')
#     print()

# hello(title="Mr.", firstName="Mohit")
# hello(firstName="Vivek", lastName="Giri")


# Nested Function

# def x():
#     """ This is x() function which has 2 more function defination in side a function """
    
    # def y():
    #     print("This is a y() function")


    # def z():
    #     print("This is z() function")

    # z()
    # print('this is a x() function')

    # y()




# print(str(input("Enter your name")))


# Higher Order Function = 1. accepts a function as an argument
#                        2. return a function as output


# 1. function as an argument
# def textToUpper(text):
#     return text.upper()

# def textToLower(text):
#     return text.lower()


# def hello(function):
#     text = function("Hello")
#     print(text)

#textToUpper
# hello(textToUpper)

# 2. return a function


# def divisor(x):
    
#     def dividend(y):
#         return y/x

#     return dividend

# x = divisor(2)
# print(x(10))


# x = divisor(5)
# print(x(50))

# 2 ^ 2
# def nthPower(exponent):
#     def powerOf(base):
#         return pow(base, exponent)
    
#     return powerOf



# square = nthPower(2)

# del nthPower

# print(square(9))

# cube = nthPower(3)
# print(cube(3))
# print(square(2))

# fourthPower = nthPower(4)
# print(fourthPower(4))
