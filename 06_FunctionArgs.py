# lst = [10, 20, 30, 40]
# a, *b, c = lst


# print(a, b, c)


# for _ in range(5):
#     print("Hello")




# def add(a, b):
#     return a + b

# lst = [1, 2]

# print(add(*lst))



# def add(a, b, *data):
#     print(f"{data = }")
#     sum = a + b
#     for x in data:
#         sum += x
#     return sum  

# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4))



def PrintEmp(ceo, cto, **data):
    print(f"CEO: {ceo}")
    print(f"CTO: {cto}")
    for pos, name in data.items():
        print(f"{pos.upper()}: {name}")

PrintEmp("Alice", "Bob")
PrintEmp(cto="Pravin", ceo="Rakesh")
PrintEmp("Alice", "Bob", cfo = "Charlie", hr = "David")
