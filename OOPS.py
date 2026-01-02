# OOPS [Object-oriented Programmings] [object,Class,*Inheritance,*Polymorphism,*Encapsulation,Abstraction]
"""
The main benefits of using OOP in Python include:-
Improved Code Structure and Organization: OOP provides a clear structure to programs by grouping related data (attributes) and behaviors (methods) into self-contained units called objects.
Code Reusability: Through the principle of inheritance, new classes can acquire properties and methods from existing "parent" classes, allowing developers to reuse common logic and reducing code duplication (the DRY principle - Don't Repeat Yourself).
Easier Maintenance and Debugging: The self-contained nature of objects makes troubleshooting simpler. When an issue arises, developers can focus on the specific object or class where the problem is occurring, rather than sifting through the entire program, which streamlines maintenance and debugging.
Scalability and Flexibility: OOP makes it easier to expand system functionalities independently. The use of concepts like polymorphism (allowing objects of different types to be treated as instances of a common type) enables developers to write code that can accommodate changing requirements without extensive modifications.
Enhanced Security (Data Protection): Encapsulation allows for the bundling of data and methods within a class while restricting access to some components. This control over data access helps prevent unintended corruption and enhances program security.
Modeling Real-World Concepts: OOP allows developers to model real-world entities and their interactions intuitively using classes and objects. This approach provides a more natural way of thinking about and solving problems, making the design process more straightforward.
Increased Productivity: By leveraging reusable code libraries and focusing on individual, modular components, programmers can construct new programs more quickly. 
"""

# Functions In OOPS called as Methods
# CLASS AND OBJECTS

#  [  A class is a collection of objects.
#     A class contains the blueprints or the prototype from which the objects are being created.
#     It is a logical entity that contains some attributes and methods.  ]

#  [  The object is an entity that has a state and behavior associated with it.
#     It may be any real-world object like a mouse, keyboard, chair, table, pen, etc.
#     Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.  ]
x
1- Polymorphysm - one name multiple form
2- encapsulation: hiding data and allowing controlled access
3- inheritance: reuse properties/methods form a parent class
4- abstraction: hiding unncessary details • I
"""
class Employee:
def __init__(self, name, age,salary):
self.name = name
self.age = age
self.salary = 20000
E1 = Employee("XYZ", 23, 20000)
# E1 is the instance of class Employee.
#__init__ allocates memory for E1.
print(E1.name)
print(E1.age)
print(E1.salary)
"""
"""
class Pound():
    value=1
    colour="Gold"
    num_edge=1
    diameter=2.5 #mm
    thickness=3.15 #mm
    head= True

coin1=Pound
print(coin1.colour)
print(coin1.value)
coin2=Pound
coin1.value=2
print(coin1.value)
print(coin2.head)
"""

# ENCAPSULATION
"""
import random
class Pound():
    def __init__(self,rare=False):      #constructor-This method is automatically called to allocate memory when a new object/instance of a class is created.All classes have the__init__ method.
        self.rare=rare                  #The self variable In Python, this is explicitly included as the first parameter. in the init method refers to the newly created object.
        if self.rare:
            self.value=1.25
        else:
            self.value=1

        self.colour = "Gold"
        self.num_edge = 1
        self.diameter = 2.5  # mm
        self.thickness = 3.15  # mm
        self.head = True

    def __del__(self):                           #Destructor
        print("coin spent!")

    def rust(self):
        self.colour="Greenish"
    def flip(self):
        head_option=[True,False]
        choice=random.choice(head_option)
        self.head=choice

a=coin1=Pound()
b=coin2=Pound(rare=True)
print(coin1.colour)
coin1.rust()
print(coin1.colour)
print(coin1.value)
print(coin2.value)
print(coin1.head)
coin1.flip()
print(coin1.head)
coin1.__del__()
"""

# INHERITANCE
"""
import random
class Coin:
    def __init__(self,rare=False,clean=True,heads=True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare=rare
        self.is_clean=clean
        self.is_heads=heads

        if self.is_rare:
            self.value=self.original_value * 1.25
        else:
            self.value=self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour=self.clean_colour

    def __del__(self):                        # Destructor
        print("coin spent!")

    def flip(self):
        head_option = [True, False]
        choice = random.choice(head_option)
        self.head = choice



class Pound(Coin):
    def __init__(self):
        data={
            "original_value":1,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edge": 1,
            "diameter": 22.5,
            "thickness":3.15,
            "mass":9.5
             }
        super().__init__(**data)

one_pound_coin=Pound()
print(one_pound_coin.colour)
one_pound_coin.rust()
print(one_pound_coin.colour)
"""

 # POLYMORPHISM
"""
import random
class Coin:
    def __init__(self,rare=False,clean=True,heads=True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare=rare
        self.is_clean=clean
        self.is_heads=heads

        if self.is_rare:
            self.value=self.original_value * 1.25
        else:
            self.value=self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour=self.clean_colour

    def __del__(self):                        # Destructor
        print("coin spent!")

    def flip(self):
        head_option = [True, False]
        choice = random.choice(head_option)
        self.head = choice
    def __str__(self):
        if self.original_value >= 1 :
            return ("{} pound coin".format(int(self.original_value)))
        else:
            return ("{} pence coin".format(self.original_value * 100))

class One_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edge": 1,
            "diameter": 20.3,
            "thickness":1.52,
            "mass":3.56
             }
        super().__init__(**data)
class Two_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edge": 1,
            "diameter": 25.9,
            "thickness":1.85,
            "mass":7.12
             }
        super().__init__(**data)
class Five_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edge": 1,
            "diameter": 18.0,
            "thickness":1.77,
            "mass":3.25
             }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

class Ten_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edge": 1,
            "diameter": 24.5,
            "thickness":1.85,
            "mass":6.50
             }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour
class Twenty_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edge": 7,
            "diameter": 21.4,
            "thickness":1.7,
            "mass":5.00
             }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour
class Fifty_Pence(Coin):
    def __init__(self):
        data={
            "original_value":0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edge": 7,
            "diameter": 27.3,
            "thickness":1.78,
            "mass":8.00
             }
        super().__init__(**data)

        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour
class One_Pound(Coin):
    def __init__(self):
        data={
            "original_value":1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edge": 1,
            "diameter": 22.5,
            "thickness":3.15,
            "mass":9.5
             }
        super().__init__(**data)

class Two_Pound(Coin):
    def __init__(self):
        data={
            "original_value":2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": "greenish",
            "num_edge": 1,
            "diameter": 28.4,
            "thickness":2.50,
            "mass":12.00
             }
        super().__init__(**data)
coins=[One_Pence(),Two_Pence(),Five_Pence(),Ten_Pence(),Twenty_Pence(),Fifty_Pence(),One_Pound(),Two_Pound()]
for coin in coins:
    arguments = [coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.num_edge,coin.mass]
    string="{} :- [ Colour:{} , Value:{} , Diameter:{} , Thickness:{} , Num_edge:{} , Mass:{} ]".format(*arguments)
    print(string)
"""


