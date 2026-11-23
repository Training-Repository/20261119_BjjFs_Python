from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def Speak(self):
        pass

    @abstractmethod
    def Eat(self):
        pass

#----------------

class Dog(Animal):
    def Speak(self):
        print("Bark");

    def Eat(self):
        print("Bite")

class Cow(Animal):
    def Speak(self):
        print("Moo");

    def Eat(self):
        print("Munch")

#--------

def Communicate(obj:Animal):
    print("Communicate -> ", end="")
    obj.Speak()

from random import randint

match randint(1, 2):
    case 1:
        obj = Dog();

    case 2:
        obj = Cow();

Communicate(obj)

print("="*40)
an1 = Animal()

an1.Speak()

d1 = Dog()
        

