a, b, c = map(int, input().split())
k = int(input())
cnt = 0

while not (a < b < c):
    cnt += 1
    if a >= b:
        b *= 2
    elif b >= c:
        c *= 2
    if cnt > k:
        print("No")
        exit(0)

print("Yes")