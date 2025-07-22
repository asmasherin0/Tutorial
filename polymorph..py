# method overloading
class num:
    def add(self,a,b):
        print( a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=num()
obj.add(2,3,2)


# byusingdefaultarguments
# class num:
#     def add(self,a,b,c=None):
#         if c==None:
#             print(a+b)
#         else:
#             print(a+b+c)
# obj=num()
# obj.add(2,3,4)
# obj.add(2,3)


# class num:
#     def add(self,a,b,c=0):
#         if c==0:
#             print(a+b)
#         else:
#             print(a+b+c)
# obj=num()
# obj.add(2,3,4)
# obj.add(2,3)


# class A:
#     def funt1(self):
#         print("func1 is working")
#
#     def funt2(self):
#         print("func2 is working")
# class B(A):
#     def funt3(self):
#         print("func3 is working")
#
#     def funt4(self):
#         print("func4 is working")
# obj = B()
# obj.funt1()
# obj.funt2()
# obj.funt3()
# obj.funt4()


# class A:
#     def funt1(self):
#         print("func1 is working")
#     def funt(self):
#         print("func2 is working")


# class B(A):
#     def funt3(self):
#         print("func3 is working")
#     def funt(self):
#         print("func4 is working")
#         super().funt()
# obj = B()
# obj.funt()


# operatoroverloading
# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __add__(self,p2):
#         print("add operator is called")
#         final_price=self.price+p2.price
#         print("final price is:",final_price)
#     def __sub__(self, other):
#         print("sub is called")
#         final_price = self.price - p2.price
#         print("final price is:", final_price)
# p1=product("pen",10)
# p2=product("pencil",5)
# p1-p2





















