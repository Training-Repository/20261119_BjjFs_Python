__all__ = ["greet", "greetName", "greetInteractive", "BuildMsg"]

def greet():
    print("Hi there!")

def greetName(name):
    greeting = "Hello"
    finalMsg = BuildMsg(greeting, name)
    print(finalMsg)

def BuildMsg(greeting, name):
    return f"{greeting}, {name}!"

def greetInteractive():
    name = input("Enter your name: ")
    greeting = "Hey"
    finalMsg = BuildMsg(greeting, name)
    print(finalMsg)

def TestMethods():
    greet()
    greetName("Alice")
    greetInteractive()

print(f"{__name__ = }")

if __name__ == "__main__":
    TestMethods()
