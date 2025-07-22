# a=lambda x,y:x+y
# print(a(5,5))
#
#
# b=lambda x:x*x
# print(b(5))

# a=[1,2,3,4,5]
# c=map(lambda x:x*x,a)
# print(list(c))
#
# a=(1,2,3,4,5)
# c=map(lambda x:x*x,a)
# print(tuple(c))



# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(lambda x:x%2!=0,a)
# print(tuple(b))


from functools import reduce
a=[1,2,3,4,5]
b=reduce(lambda x,y:x+y,a)
print(b)

#
# a=lambda x,y:x*y
# print(a(5,7))


# def a(b):
#     return b*b
# print(a(5))


# a=lambda x:x*x
# print(a(6))
#
# b=lambda x,y,z:x+y+z
# print(b(2,3,4))

# a=[2,3,4,5]
# result=[]
# for i in a:
#     result.append(i*i)
# print(result)


# a=[2,3,4,5]
# b=map(lambda x:x*x,a)
# print(list(b))

# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(lambda x:x%2==0,a)
# print(list(b))

from functools import reduce
a=[1,2,3,4,5]
b=reduce(lambda x,y:x+y,a)
print(b)





































