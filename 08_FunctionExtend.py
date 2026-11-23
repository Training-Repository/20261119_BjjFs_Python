# def add(a: int, b: int):
#     return a + b

# #----

# fn1 = add

# def add_ex(a, b):
#     print("Add called")
#     return fn1(a, b)

# fn2 = add_ex
# add = fn2

# add(1, 2)
# add("Test", "string")

#---------------------------------------

#region Closure
# def powerOf(base: int, exponent: int):
#     return base ** exponent

# def Exponent(exp: int):
#     def powerOf(base: int):
#         return base ** exp
#     return powerOf

# # sq = Exponent(2)
# # print(sq(10))

# # cb = Exponent(3)
# # print(cb(10))

# # print(cb(10), sq(10))

# tools = [Exponent(0), Exponent(1), Exponent(2), Exponent(3)]

# for fn in tools:
#     print(fn(10))
#endregion



#region Fn2FnDecorator

# def greet():
#     """Greets the person"""
#     print("Hi there")

# def add(a, b):
#     '''Retuns the sum
#     Accepts 2 args
#     returns a simgle obj of the type of arg sent'''
#     return a + b

# def div(a, b):
#     '''Retuns the quotient
#     Accepts 2 args; Ensure 'b' is not ZERO
#     returns a simgle obj of the type of arg sent'''
#     if b == 0:
#         print("Incorrect argument\nCheck usage\n", div.__doc__)
#     return a + b

# print(f"{greet.__doc__ = }")
# print(f"{add.__doc__ = }")
# div(1, 0)

# # fn = greet
# # fn2 = add

# # def wrapper():
# #     print("Greet method called")
# #     fn()

# # def wrapper2(a, b):
# #     print("Add method called")
# #     res = fn2(a, b)
# #     return res

# # greet = wrapper
# # add = wrapper2

# #-----------------

# def Logger(fn):
#     def wrapper(*vArgs, **kwArgs):
#         wrapper.__doc__ = fn.__doc__
#         print(f"{fn.__name__} method called")
#         res = fn(*vArgs, **kwArgs)
#         return res
#     return wrapper

# greet = Logger(greet)
# add = Logger(add)



# #---------------
# greet()

# print(add(1, 2))

# print(f"{greet.__doc__ = }")
# print(f"{add.__doc__ = }")

#endregion

#region Fn2FnDecorator_Revised

def Logger(fn):
    def wrapper(*vArgs, **kwArgs):
        wrapper.__doc__ = fn.__doc__
        print(f"{fn.__name__} method called")
        res = fn(*vArgs, **kwArgs)
        return res
    return wrapper


#---------------

@Logger
def greet():
    """Greets the person"""
    print("Hi there")

@Logger
def add(a, b):
    '''Retuns the sum
    Accepts 2 args
    returns a simgle obj of the type of arg sent'''
    return a + b

@Logger
def div(a, b):
    '''Retuns the quotient
    Accepts 2 args; Ensure 'b' is not ZERO
    returns a simgle obj of the type of arg sent'''
    if b == 0:
        print("Incorrect argument\nCheck usage\n", div.__doc__)
    return a + b


# div = Logger(div)

#-----------------

greet()

print(add(1, 2))

print(f"{greet.__doc__ = }")
print(f"{add.__doc__ = }")

#endregion