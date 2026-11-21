def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        # print("Error: Division by zero is not allowed.")
        raise Exception("Will NOT allow Division by zero")
    result = a / b
    # print("Completed Calculation")
    return result