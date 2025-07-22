# filecreation
# f=open("F:sample.docx", 'w')
# f.close()

# writefun
# f=open("sample.txt", 'w')
# f.write("helloo")
# f.close()

# appendfun
# f=open("sample.txt", 'a')
# f.write("helooooo\n")
# f.close()


# readfun6
# f=open("sample.txt",'r')
# a=f.read()
# print(a)
# f.close()

# f=open("sample.txt",'r')
# print(f.read())
# f.close()

# file=open('abc.txt','r')
# content=file.read()
# print(content)
# file.close()


# file=open('abc.txt','r')
# content=file.readline()
# print(content)
# file.close()


# file=open('abc.txt','r')
# content=file.readlines()
# print(content)
# file.close()

# file=open('abc.txt','w')
# file.write("good morning\n")
# file.write("good night\n")
# file.close()
#
# file=open("abc.txt",'a')
# file.write("hai")
# file.close()


# with open('abc.txt','r') as file:
#     content=file.read()
#     print(content)


# try:
#     file=open("xyz.txt",'r')
#     content=file.read()
#     print( content)
# except FileNotFoundError:
#     print("file does not exist")
# except IOError:
#     print("io error occured")

with open('sample.txt','r') as file:
    content=file.read()
    print(content)










































