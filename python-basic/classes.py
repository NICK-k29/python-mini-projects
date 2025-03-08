# class with instance
class  Student:
    def __init__(self,name):
        self.name=name

student1 = Student("nitesh")
print("\n")
print(student1.name)

# without any variable and methods
class Vehicle:
    pass

# EX 3
class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

class Bus(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)

Bus1 = Bus("Volvo", 2025)
print("\n")
print("Year = ",Bus1.year)
print("Brand = ",Bus1.brand)

# Ex 4 class inheritance

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
      print(f"{self.name} is eating")

class dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name,age)
        self.breed = breed

    def bark(self):
      print(f"{self.name} is barking")

dog1 = dog("Tyson",3,"husky")
print("\n")
print("name =",dog1.name)
print("age =",dog1.age)
print("breed =",dog1.breed)
dog1.bark()
dog1.eat()

# EX 5

class planet:
    type="Water"
    def __init__(self,name,size):
        self.name = name
        self.size = size
p1=planet("Earth","Large")
p2=planet("mars","small")
print("\n")
print(planet.type)
print(p1.type)
print(p2.type)

# Ex 6

class Shape:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type
    def area(self):
        pass
class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color, "Square")
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2
square = Square("Red", 5)
print("\n")
print(square.color)
print(square.shape_type)
print(square.area())

# ex 7 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
car = Car("Toyota", "SUV")
print("\n")
print(isinstance(car, Car))

# ex 8 

class Vehicle:
    pass
class School_bus(Vehicle):
    pass
school_bus = School_bus()
print("\n")
print(isinstance(school_bus, School_bus))