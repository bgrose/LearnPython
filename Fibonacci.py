# Bradley Grose

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# Testing Code
import types

if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    i = 0
    for n in fib():
        print(n)
        i += 1
        if i == 10:
            break
