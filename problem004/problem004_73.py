N = int(input())

for i in range(N):
    a = list(map(int, input().split()))
    a.sort()
    if (a[2] ** 2 == a[0] ** 2 + a[1] ** 2):
        print("YES")
    else:
        print("NO")
    
