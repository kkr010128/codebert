n = int(input())
X = [[] for _ in range(n)]
for i in range(n):
    x,l = list(map(int, input().split()))
    X[i] = [x-l,x+l]

X.sort(key = lambda x: x[1])
cnt = 1
mx = X[0][1]
for i in range(1,n):
    if mx <= X[i][0]:
        cnt += 1
        mx = X[i][1]
print(cnt)