# righthalf
# rows=5
# for i in range( rows):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()


# lefthalf
# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=' ')
#     for k in range(i+1):
#         print("*",end=' ')
#     print()

# # full
# rows=5
# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for k in range(1, 2 * i):
#         print("*", end="")
#     print()

# n=5
# for i in range(1,n):
#     for j in range(i,n):
#         print("",end=' ')
#     for k in range(i):
#         print("*",end =' ')
#     print()

#
# # invertedright
# rows=5
# for i in range(rows, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()



# invertedleft
# rows=5
# for i in range(rows, 0, -1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for k in range(1, i + 1):
#         print("*", end="")
#     print()
#


# invertedfull
# rows=5
# for i in range(rows, 0, -1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for k in range(1, 2 * i):
#         print("*", end="")
#     print()


# #RhombusPattern
# rows=5
# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for k in range(1, rows + 1):
#         print("*", end="")
#     print()


# diamondpattern
rows=5
# # Upper half
# for i in range(1, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()
# # Lower half
# for i in range(rows - 1, 0, -1):
#     for j in range(1, rows - i + 1):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#        print()




# HourglassPattern
# # Upper half (inverted full pyramid)
# rows=5
# for i in range(rows, 0, -1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for k in range(1, 2 * i):
#         print("*", end="")
#     print()
# # Lower half (full pyramid, starting from second row)
# for i in range(2, rows + 1):
#     for j in range(1, rows - i + 1):
#         print(" ", end="")
#     for k in range(1, 2 * i):
#         print("*", end="")
#     print()



# HollowSquarePattern
# rows=5
# for i in range(1, rows + 1):
#     for j in range(1, rows + 1):
#         if i == 1 or i == rows or j == 1 or j == rows:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
#


















