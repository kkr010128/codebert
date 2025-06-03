x,k = map(int,input().split())
y = x % k
print(min(y,k-y))