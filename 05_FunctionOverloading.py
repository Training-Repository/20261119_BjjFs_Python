# def add1(a, b):
#     return a + b


# def add2(a, b, c=0):
#     return a + b + c

# def add(*args):
#     args_len = len(args)
#     match args_len: 
#         case 2:
#             return add1(*args)
#         case 3:
#             return add2(*args)
#         case _:
#             raise TypeError(f"add() takes 2 or 3 positional arguments but {args_len} were given")

# print(add(1, 2))
# print(add(1, 2, 3))

# print(type(add))

from multipledispatch import dispatch

@dispatch(int, int)
def add(a: int, b: int) -> int:
    print("Int version called")
    return a + b

@dispatch(float, float)
def add(a: float, b: float) -> float:
    print("Float version called")
    return a + b

@dispatch(str, str)
def add(a: str, b: str) -> str:
    print("String version called")
    return a + b

print(add(1, 2))
print(add(1.1, 2.2))
print(add("Hello", "World"))

