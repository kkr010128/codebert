n = int(input())

A = {}

for i in range(n):
    a, b = input().split()
    if a[0] == "i":
        A[b] = 1
    elif a[0] == "f":
        if b in A:
            print("yes")
        else:
            print("no") 

