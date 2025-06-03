N = int(input())

c = 0
for _ in range(N):
    if len(set(input().split())) == 1:
        c += 1
        if 3 <= c:
            print("Yes")
            exit()
    else:
        c = 0
else:
    print("No")
