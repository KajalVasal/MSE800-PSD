# Factory Method Pattern Example
A simple Python example showing the Factory Method 
design pattern using animals.

## What is it?
The Factory Method pattern defines an interface for 
creating objects, but lets subclasses decide which 
class to instantiate. This keeps object creation
decoupled from the client code.

## Classes
### Abstract Classes
- **Factory**: Abstract creator with abstract method `create_product()`.
- **Animals**: Abstract product with abstract method `run()`.

### Concrete Classes
- **AnimalFactory**: Creates `Dog` or `Cat` based on the `kind` parameter.
- **DogFactory**: create `Dog` objects.
- **CatFactory**: create `Cat` objects.
- **Dog**: Concrete product that implements `run()`.
- **Cat**: Concrete product that implements `run()`.

## How to Run

python Activity 1.py