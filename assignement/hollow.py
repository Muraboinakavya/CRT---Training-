n = int(input("Enter the n value:"))
for i in range(n):
    print(" " * i, end="")
    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print("*")
    else:
        inner_spaces = 2 * (n - i - 1) - 1
        print("*" + " " * inner_spaces + "*")