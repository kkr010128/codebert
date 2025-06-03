a = list(map(int,input().split()))

print(a[0]*a[1] if a[0] <= 9 and a[1] <= 9 else -1)