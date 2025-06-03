N = int(input())
for i in range(N):
    a, b, c = map(int, input().split())
    sort = sorted([a, b, c])
    if sort[0]**2 + sort[1]**2 == sort[2]**2:
        print("YES")
    else:
        print("NO")