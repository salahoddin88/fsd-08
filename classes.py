""" 
    class = real world entity blueprint, layout, structure, collection of objects
    object = small entity

    attributes - variables
    behaviour - method
    class ClassName:
        pass
"""

# class Home:

#     member = 5      # class variable
  
#     def __init__(self, name):       # constructor 
#         self.name = name        # instance variable
#         print(f"welcome {name}, play automated Song")

#     def LivingRoom(self):
#         print(f'{self.name} is in living Room')

#     def Library(self):
#         print(f'{self.name} is in Library')

#     def Gym(self, clothing):
#         print(f'{self.name} is in gym, please wear {clothing}')


# # amol = Home('Amol')
# guest = Home('Mohit')

# print(guest.member)
# print(guest.name)
# # guest.LivingRoom()
# # guest.Library()
# # guest.Gym('Track suit')



# # amolSbrother.Gym()



# class Calc:

#     def addition(self, num1, num2):
#         return int(num1) + int(num2)

#     def sub(self, num1, num2):
#         return int(num1) - int(num2)


# obj1 = Calc()
# additionResponse = obj1.addition(25,10)
# print(additionResponse)
# print(obj1.sub(5,2))


class GroundFloor:
    
    member = 5

    def __init__(self):
        print('Play random song')


    def livingRoom(self):
        print('Person is in living room')


    def kitchen(self):
        print('Person is in kitchen')        



class FirstFloor(GroundFloor):
    
    def __init__(self):
        print('Play random song 2')


    def bedRoom(self):
        super().kitchen()
        print('Person is in bed room')


class SecondFloor(FirstFloor):
    
    def __init__(self):
        print('Play random song 3')


    def bedRoom2(self):
        super().bedRoom()
        print("Person is in 2nd floor's bed room")


person = SecondFloor()
person.bedRoom2()
person.bedRoom()

# person = GroundFloor()
# person.livingRoom()
# person.kitchen()

# person = FirstFloor()
# print(person.member)
# person.livingRoom()
# person.kitchen()
# person.bedRoom()

# person = SecondFloor()
# person.bedRoom()
# person.kitchen()
# person.bedRoom2()


# class Vehicle:

#     def __init__(self):
#         print('This is Vehicle\'s __init__')

#     def model(self):
#         print('This is Model')


# class Car:
    
#     def __init__(self):
#         print('This is Car\'s __init__')

#     def name(self):
#         print('This is TATA NANO')


# class Tata(Car, Vehicle, SecondFloor):

#     def __init__(self):
#         print('This is Tata\'s __init__')
    


# tata = Tata()
# tata.model()
# tata.name()
