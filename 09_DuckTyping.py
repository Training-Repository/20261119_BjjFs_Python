class Animal:
    def Speak(self):
        print("Speaking...")

    def Eat(self):
        print("Eating")

#----------------

class Dog:
    # def Speak(self):
    #     print("Bark");

    def Eat(self):
        print("Bite")

class Cow:
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


        

