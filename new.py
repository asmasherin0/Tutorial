# # sum
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# sum=int(a)+int(b)
# print("result=" +str(sum))

# #average
# num1=int((input("enter 3 numbers")))
# num2=int(input())
# num3=int(input())
# average=(num1+num2+num3)/3
# print("average ="+str(average))

#swapping
# a=10
# b=15
# c=a
# a=b
# b=c
# print("first number ="+ str(a) ,"second number=" +str(b))

# a="hello"
# # print(type(a))   str
# # print(len(a))  5
# # print(a[2])  l
# # print(a[2:5])   llo
# # print(a[1:3])  el
# print(a[1:4])    ell


# #list
# values=["apple","orange","banana"]
# values=values+["anar","carrot"]
# values.append("hai")
# values.append(int(input("enter a value")))
# print(values)


# #if
# num=int(input("enter a number"))
# if num<0:
#     print("negative")
# elif num==0:
#     print("zero")
# else:
#     print("positive")


#while
# i=0
# while i<=20:
#     print(i)
#     i+=1

#
# i="*"
# while i<***:
#     print("i")
#     i+=1


#for loop
# values=["apple","banana","cherry"]
# for x in values:
#     print(x[2:5])
#     print(x)
# print(values)

# for x in range(7):
#     print(x)
# for x in range(2,5):
#     print(x)
# for x in range(2,10,3):
#       print(x)
# for x in range(10,50,5):
#       print(x)


#function
# def values():
#     print("good")
# values()

# def hey(name):
#     print("my name is " +name)
# hey("asma sherin")

# def ache(name):
#     print("my name is "+ name)
# value = "asma sherin"
# ache(value)

#global variable
# value=10
# def sample():
#     print(value)
# print(value)
# sample()

#local variable
# value=10
# def sample():
#     print(30)
# sample()
# print(value)

# keyword arguments
# def sample(name,age):
#     print(name,age)
# sample("asma",55)

# def sample(name,age):
#     print(name,age)
# sample(age=55,name="heeeeeey")


#sum
# def sample(num1,num2):
#     sum=num1+num2
#     return sum
# result=sample(10,2)
# print(result)


#dictionary
# value={"name":"asma","age":12}
# print(value)
# print(value.get("age"))


# #modules
# def check():
#     num=int(input("enter a number"))
#     if num<0:
#         print("negative")
#     elif num==0:
#         print("zero")
#     else:
#         print("positive")
# check()


# # exception
# b=10
# try:
#     a=20/b
#     print(a)
#     print("try completed")
# except ZeroDivisionError:
#     print("cant divide by zero")
# print("program completed")


# # scope
# def check_scope():
#     def do_local():
#         test="local test"
#     def do_non_local():
#         test="non local test"
#     def do_global():
#         test ="global test"
#     test="default"
#     do_local()
#     print("test value after do_local: "+ test)
# check_scope()


# oops

# class
# class Mysample:
#     def heey(self):
#         print("hellooooo")
# x=Mysample()
# x.heey()
#
#
# class Mysample:
#     def heey(self,n):
#         print("hellooooo" + n)
# x=Mysample()
# name="asma"
# x.heey(name)


# # inheritance
# class baseclass:
#     def display(self):
#         print("hey")
# class subclass(baseclass):
#     def welcome(self):
#         print("good morning")
# x=baseclass()
# x.display()
#
# y=subclass()
# y.welcome()
# y.display()
#


# class first:
#     def display(self):
#         print("fine")
# class second:
#     def show(self):
#         print("byyy")
# class third(first,second):
#     def thi(self):
#         print("third")
# x=third()
# x.thi()
# x.display()
# print(third.mro())


# datetime
# import datetime
# print(datetime.datetime.now())
# print(datetime.date.today())
#
# import datetime
# now=datetime.datetime.now()
# print(now.strftime("%d/%m/%y"))
# print(now.strftime("%d/%m/%Y"))


# import datetime
# x=datetime.datetime(2004,5,15)
# print(x)

# import datetime
# x=datetime.datetime(2004,5,15)
# y=datetime.datetime(2025,6,22)
# dif=y-x
# print(dif)

# file
# f=open("hey.py","w")
# f.write("print('hhhhh')")
# f.close()

# with open("hey.py","r") as f:
#     x=f.read()
# print(x)



# tkinder widgets

# from tkinter import *
# window=Tk()
# window.mainloop()
# print("hellooo")



# from tkinter import *
# window=Tk()
# button=Button(window,text="ok",width=30,height=30,bg="yellow",fg="blue")
# label=Label(window,text="welcome")
# button.pack()
# label.pack()
# window.mainloop()
# print("hellooo")







































