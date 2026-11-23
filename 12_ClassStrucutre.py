from random import randint

class Car:
    """Make, Model, Year, Colour"""
    count = 0

    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.__colour = colour
        self.speed = 0
        self.bRunning = False
        Car.count += 1
        self.serialNo = Car.GenSerial()

    def __str__(self):
        return f"[{self.make}, {self.model}, {self.year}, {self.__colour}]"

    def __repr__(self):
        return f"[{self.__class__.__name__} : {self.count}][{self.make}, {self.model}, {self.year}, {self.__colour}, {self.serialNo}]"

    def start(self):
        if not self.bRunning:
            print(f"{self.__colour} {self.model} starting up.")
            self.bRunning = True
        else:
            print(f"{self.__colour} {self.model} is already running.")

    def stop(self):
        if self.bRunning == True and self.speed == 0:
            print(f"{self.__colour} {self.model} stopping.")
            self.bRunning = False
        else:
            print(f"{self.__colour} {self.model} not in a state to stop.")

    def accelerate(self):
        if self.bRunning == True:
            self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    @classmethod
    def GetCount(cls):
        return cls.count

    @staticmethod
    def GenSerial():
        return randint(1000, 9999)


#################################################



def Test1():
    print(Car.GetCount())
    c1 = Car("Honda", "Accord", 2026, "White")
    c2 = Car("Mazda", "Miata", 2025, "Yellow")

    print(c1.make, c2.make)
    # print(c1.display())
    # print(c2.display())
    print("-"*20)
    print(c1)
    print(str(c1))
    print(c1.__str__())
    print(c2.__repr__())

def Test2():
    c1 = Car("Honda", "Accord", 2026, "White")
    c2 = Car("Mazda", "Miata", 2025, "Yellow")

    # print(c2.__colour)
    c2.__colour = "Blue"
    print(f"{c2._Car__colour = }")
    print(c2.__colour)

    print(c2)

    print(dir(c2))

if __name__ == '__main__':
    # Test2()
    lan = "BFLPUN2026000731"
    print(lan[:3], lan[-3:], lan[3:6].lower(), lan[100:] == "")
    print(f"{lan[100:] = }")