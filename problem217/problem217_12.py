n = int(input())
a = list(map(int, input().split()))
x = "APPROVED"
for i in range(n):
    if a[i] == (2 * int(a[i] / 2)):
        if a[i] != (3 * int(a[i] / 3)):
            if a[i] != (5 * int(a[i] / 5)):
                x = "DENIED"
print(str(x))