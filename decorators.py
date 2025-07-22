# def name():
#     return "hello"
# name()


# def upper_decorate(func):
#     def inner():
#         result=func()
#         return result.upper()
#     return inner
# def name():
#     return "hello"
# f=upper_decorate(name)
# print(f())



# def upper_decorate(func):
#     def inner():
#         result=func()
#         return result.upper()
#     return inner
# @upper_decorate
# def name():
#     return "hello"
# print(name())


def upper_decorate(func):
    def inner(name):
        result=func(name)
        return result.upper()
    return inner
@upper_decorate
def newfunc(name):
    return "hello "+name
print(newfunc("asma sherin"))











