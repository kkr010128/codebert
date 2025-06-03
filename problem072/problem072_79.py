n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    d1, d2 = d[i]
    if d1 == d2:
        cnt += 1
        if cnt == 3:
            print("Yes")
            exit(0)
    else:
        cnt = 0

print("No")