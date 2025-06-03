N,M = map(int,input().split())
A = list(map(int,input().split()))

homeworks = 0
for i in A:
    homeworks += i

if N >= homeworks:
    print(N-homeworks)
else:
    print(-1)
