def add(a: int, b: int):
    return a + b

#----

fn1 = add

def add_ex(a, b):
    print("Add called")
    return fn1(a, b)

fn2 = add_ex
add = fn2

add(1, 2)
add("Test", "string")