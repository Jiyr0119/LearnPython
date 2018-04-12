L = [x*x for x in range(10)]
g = (x*x for x in range(10))

# print(L)
# print(g)
#
# for n in g:
#     print(n)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield (3)
    print("step 3")
    yield (5)

o = fib(10)

while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

