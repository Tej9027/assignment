from abc import ABC, abstractmethod
class Animal(ABC):
  def __init__(self,name):
    self.name=name

  @abstractmethod
  def sound(self):
    pass

class Dog(Animal):
  def sound(self):
    return "Woof!"

class Cat(Animal):
  def sound(self):
    return "Meow!"

def animal_sound(animal):
  print(f"{animal.name} says: {animal.sound()}")

dog=Dog("Buddy")
cat=Cat("Whiskers")

animal_sound(dog)
animal_sound(cat)