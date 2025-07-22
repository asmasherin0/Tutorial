import sys
print(sys.version)


# globalvariable
# x="awesome"
# def myfunc():
#     print("python is ",x)
# myfunc()

# localvariable
# x = "awesome"
# def myfunc():
#     x = "fantastic"
#     print("python is ",x)
# myfunc()
# print("python is ", x)

# globalkeyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)


# import random
# print(random.randrange(1,10))












