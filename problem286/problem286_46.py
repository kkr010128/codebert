n = list(map(int,input().split()))
if max(n)>9:
    print(-1)
else:
    print(n[0]*n[1])