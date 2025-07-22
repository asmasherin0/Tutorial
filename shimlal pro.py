# for x in range(1,10):
#     print(x)



# a="hello"
# print(a[::-1])


# my_list = [1, 2, 3, 4]
# a = iter(my_list)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


def countdown(n):
    while n > 0:
        yield n
        n -= 1
gen = countdown(5)
for value in gen:
    print(value)