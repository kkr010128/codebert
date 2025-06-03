import itertools
n,m = map(int, input().split())
ball = [2*i for i in range(1,n+1)] + [(2*j)-1 for j in range(1,m+1)]

cnt = 0

for c in itertools.combinations(ball,2):
    cnt += sum(c)%2 == 0

print(cnt)