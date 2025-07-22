# tuple = ("apple", "orange", "mango")
# print(tuple)
# print(len(tuple))
# print(type(tuple))
#
# #type
# tuple =("apple",)
# print(type(tuple))
# tuple =("apple")
# print(type(tuple))
#
# #constructor
# tuple = (("apple", "orange", "mango"))
# print(tuple)
#
# #access tuple
# tuple = (("apple", "orange", "mango"))
# print(tuple[1])
# print(tuple[-1])
# print(tuple[-2])
# print(tuple[-3])
#
#
# #range
# tuple = (("apple", "orange", "mango","grapes","kiwi"))
# print(tuple[0:2])
# print(tuple[1:4])
# print(tuple[3:5])
# print(tuple[:4])
# print(tuple[:2])
# print(tuple[2:])


#check if item exists
# tuple = ("apple", "orange", "mango")
# if "apple" in tuple:
#   print("Yes, 'apple' is in the fruits tuple")


# #change tuple values
# a= ("apple", "orange", "mango")
# b=list(a)
# b[1]="anar"
# a=tuple(b)
# print(a)
#
# tup= ("apple", "orange", "mango")
# lis=list(tup)
# lis[1]="anar"
# tup=tuple(lis)
# print(tup)



thistuple=("apple", "orange", "mango")
y=list(thistuple)
y.append("kiwi")
thistuple=tuple(y)