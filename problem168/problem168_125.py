n, m = map(int,input().split())
A = tuple(map(int,input().split()))
days = 0
for i in A:
    days += i
if n < days:
    print(-1)
else:
    print(n-days)