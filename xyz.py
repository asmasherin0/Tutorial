# #change tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#add item
thistuple = ("apple", "banana", "cherry")
h = list(thistuple)
h.append("orange")
thistuple = tuple(h)
print(thistuple)
