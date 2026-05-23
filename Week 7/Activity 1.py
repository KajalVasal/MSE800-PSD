from abc import ABC, abstractmethod
# Factory Method Design Pattern
class Factory(ABC):
    # factory method
    @abstractmethod
    def create_product(self, kind=None):
        pass
# concrete factory
class AnimalFactory(Factory):
    def __init__(self):
        pass
# concrete factory method
    def create_product(self, kind=None):
        if kind == "dog":
            animal = Dog()
        elif kind == "cat":
            animal = Cat()

        return animal
# concrete factory
class DogFactory(Factory):
    
    def create_product(self, kind=None):
        return Dog()
# concrete factory
class CatFactory(Factory):
    
    def create_product(self, kind=None):
        return Cat()
# abstract product
class Animals(ABC):

    @abstractmethod
    def run(self):
        pass
# concrete product
class Dog(Animals):

    def run(self):
        print(f"I'm a Dog, I can run!!")

# concrete product
class Cat(Animals):
    def __init__(self):
        pass

    def run(self):
        print(f"I'm a Cat, I can run!!")



# client
factory = AnimalFactory()
dog = factory.create_product(kind="dog")
cat = factory.create_product(kind="cat")

dog.run()
cat.run()
