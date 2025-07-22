n=7
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# righthalf
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# invertedright
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()


# lefthalf
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=" ")
#     for k in range(i+1):
#         print("*",end=' ')
#     print()

# invertedleft
# for i in range(n):
#     for j in range(i):
#         print(' ',end=" ")
#     for k in range(i,n):
#         print("*",end=' ')
#     print()

# fullpyramid
# for i in range(n):
#     for j in range(n-i-1):
#         print('',end=" ")
#     for k in range(i+1):
#         print("*",end=' ')
#     print()

# invertedfull
# for i in range(n):
#     for j in range(i):
#         print('',end=" ")
#     for k in range(n-i):
#         print("*",end=' ')
#     print()


# rhombuspattern
# for i in range(n):
#     for j in range(n-i):
#         print('',end=" ")
#     for k in range(n):
#         print("*",end=' ')
#     print()

# # diamodpattern
# for i in range(n-1):
#     for j in range(n-i-1):
#         print('',end=" ")
#     for k in range(i+1):
#         print("*",end=' ')
#     print()
# for i in range(n):
#     for j in range(i):
#         print('',end=" ")
#     for k in range(n-i):
#         print("*",end=' ')
#     print()

# hourglass
# for i in range(n-1):
#     for j in range(i):
#         print('',end=" ")
#     for k in range(n-i):
#         print("*",end=' ')
#     print()
# for i in range(n):
#     for j in range(n-i-1):
#         print('',end=" ")
#     for k in range(i+1):
#         print("*",end=' ')
#     print()


# hollowsquare
# for i in range(n):
#     for j in range(n):
#         if (i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()


# hollowfull
# for i in range(n):
#     for j in range(n):
#         if (i==n or i==n-1 or j==0 or j==n-1):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()



# floydstriangle
# num = 1
# # for i in range(n):
# #     for j in range(i+1):
# #         print(num,end=' ')
# #         num+=1
# #     print()
#
# for i in range(n):
#     for j in range(n):
#         if ( i==n-1 ):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()
#
# for i in range(n):
#     for j in range(n-i-1):
#         print('',end=" ")
#     for k in range(i+1):
#         print("*",end=' ')
#     print()



# n=7
#
# for i in range(n):
#     for j in range(n):
#         if i+j==3 or j-i==3 or i+j==9 or i-j==3:
#             print("*", end=' ')
#         else:
#              print('',end=" ")
#     print()


# n=4
# for i in range(n*2-1):
#     for j in range((n*2-1)):
#         if i+j==n-1 or j-i==n-1 or i+j==3*(n-1) or i-j==n-1:
#             print("*", end=' ')
#         else:
#              print(' ',end=" ")
#     print()

#
# for i in range(n):
#     for j in range((n*2-1)):
#         if i+j==n-1 or j-i==n-1 or i+j==3*(n-1) or i-j==n-1 or i==3:
#             print("*", end=' ')
#         else:
#              print('',end=" ")
#     print()

# text = "Python"
#
# # for char in text:
# #     print(char)
# #
# squares = []
# for x in range(5):
#     squares.append(x**2)
# print(squares)



n=5
for i in range(n):
    for j in range(i):
        print("",end=' ')
    for k in range(i,n):
        print("*",end=' ')
    print()

    n = int(input("Enter N: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print("Sum:", sum)
