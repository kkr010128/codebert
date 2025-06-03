N = int(input())
X = []
L = []
for i in range(N):
    x, l = map(int, input().split())
    X.append(x)
    L.append(l)

# できるだけ少ないロボットを取り除いて条件を満たすようにしたい
ranges = [[x - l, x + l] for x, l in zip(X, L)]
ranges = sorted(ranges, key=lambda x:x[1])

ans = N
for i in range(1, N):
    if ranges[i][0] < ranges[i - 1][1]:
        ranges[i][1] = ranges[i - 1][1]
        ans -= 1
print(ans)
