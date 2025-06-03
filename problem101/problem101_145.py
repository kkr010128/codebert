a, b, c = map(int, input().split())
k = int(input())

if a >= b:
    while a >= b:
        if k == 0:
            print("No")
            exit()
        b *= 2
        k -= 1

if b >= c:
    while b >= c:
        if k == 0:
            print("No")
            exit()
        c *= 2
        k -= 1

print("Yes")

