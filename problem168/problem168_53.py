N,X = map(int,input().split())
Y = N - sum(map(int,input().split()))
print(("-1",Y)[Y >= 0])