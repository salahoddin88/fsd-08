"""
    1. Compile Time Error (syntax error) (developer side)
    2. Logical Errors (working code but provides a wrong output)
    3. Run Time Error (Working code but breaks at certain point) (Mistake by users)

"""

""" Custom Exception Class """
class Temprature(Exception):
    
    def __init__(self, message):
        super().__init__(message)


raise Temprature('Temprature is too hot')

try:
    print("Resource Open")
    a = 6
    b = 2
    print(a/b)
    

except Temprature as e:
    print(e)
    print('Temprature is too cold')

except Exception as e:
    print('Something went wrong')

finally:    # optional
    print("Resource Closed")


# print('Hello')
