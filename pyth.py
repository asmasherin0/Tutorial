rows = 5

print("--- Right Half Pyramid ---")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

print("\n--- Left Half Pyramid ---")
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()

print("\n--- Full Pyramid ---")
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

print("\n--- Inverted Right Half Pyramid ---")
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

print("\n--- Inverted Left Half Pyramid ---")
for i in range(rows, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()

print("\n--- Inverted Full Pyramid ---")
for i in range(rows, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

print("\n--- Rhombus Pattern ---")
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, rows + 1):
        print("*", end="")
    print()

print("\n--- Diamond Pattern ---")
# Upper half
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
# Lower half
for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

print("\n--- Hourglass Pattern ---")
# Upper half (inverted full pyramid)
for i in range(rows, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
# Lower half (full pyramid, starting from second row)
for i in range(2, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

print("\n--- Hollow Square Pattern ---")
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == 1 or i == rows or j == 1 or j == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n--- Hollow Full Pyramid ---")
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == (2 * i - 1) or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n--- Hollow Inverted Full Pyramid ---")
for i in range(rows, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == (2 * i - 1) or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n--- Hollow Diamond Pyramid ---")
# Upper half (hollow full pyramid)
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
# Lower half (hollow inverted full pyramid, starting from second last row)
for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n--- Hollow Hourglass Pattern ---")
# Upper half (hollow inverted full pyramid)
for i in range(rows, 0, -1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == (2 * i - 1) or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()
# Lower half (hollow full pyramid, starting from second row)
for i in range(2, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        if k == 1 or k == (2 * i - 1) or i == rows:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n--- Floyd's Triangle ---")
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

print("\n--- Pascal's Triangle ---")
# This is a bit more complex as it involves combinations (binomial coefficients)
# Without functions, we'll calculate binomial coefficients directly.

for i in range(rows):
    # Print leading spaces
    for j in range(1, rows - i):
        print(" ", end="")

    # Calculate and print numbers
    coef = 1 # C(n, k) starts at 1 for k=0
    for j in range(0, i + 1):
        print(coef, end=" ")
        coef = coef * (i - j) // (j + 1) # C(n, k) = C(n, k-1) * (n-k+1) / k
    print()