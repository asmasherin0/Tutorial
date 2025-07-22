def gener():
    yield 10
    yield 20
    yield 30
num=gener()
print(next(num))
print(next(num))
print(next(num))
