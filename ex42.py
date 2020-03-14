## Animal is-a object
class Animal(object):
    """description"""
    pass

## Dog is-a Animal
class Dog(Animal):
    """description"""
    def __init__(self, name):
        """docstring for __init__"""
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    """description"""
    def __init__(self, name):
        """docstring for __init__"""
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    """description"""
    def __init__(self, name):
        """docstring for __init__"""
        ## Person has-a name
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):
    """description"""
    def __init__(self, name, salary):
        """docstring for __init__"""
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    """description"""
    pass

## Salmon is Fish
class Salmon(Fish):
    """description"""
    pass
        
## Halibut is Fish
class Halibut(Fish):
    """description"""
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is Employee
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is Salmon
crouse = Salmon()

## harry is Halibut
harry = Halibut()
