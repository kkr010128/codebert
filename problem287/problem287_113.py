N = int(input())
for i in range(1, 10):
    if N % i == 0:
        j = N // i
        if 1 <= j and j <= 9:
            print("Yes")
            exit()
print("No")