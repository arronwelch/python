# recursion algorithm

####1.calls itself
####2.return condition

def func1(x):
    print(x)
    func1(x-1)
# not recursion function

def func2(x):
    if x > 0:
        print(x)
        func2(x+1)

def func3(x):
    if x > 0:
        print(x)
        func3(x-1)

def func4(x):
    if x > 0:
        func4(x-1)
        print(x)


