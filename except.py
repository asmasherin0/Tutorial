# try:
#     a=10 /0
#     print(a)
# except ZeroDivisionError:
#     print("you cant divide by zero ")
# finally:
#     print("always run")


# try:
#     num=int(input("enter the number"))
#     print(f"you entered:{num}")
# except ValueError:
#     print("invalid input!enter a number")
# finally:
#     print("always run")

# print(eval(input("enter your numbers")))


# class InvalideAgeException(Exception):
#     pass
# try:
#     num=int(input("enter the number"))
#     if num<18:
#         raise InvalideAgeException
#     else:
#         print("eligible to vote")
# except InvalideAgeException:
#     print("Exception occured.invalid age")




class InvalidAGE(Exception):
    pass
try:
    num=int(input("enter num"))
    if num<18:
        raise InvalidAGE
    else:
        print("eligible")
except InvalidAGE:
    print("exception occured")


















