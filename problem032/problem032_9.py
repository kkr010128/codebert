import math
n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
D = [abs(X[i]-Y[i]) for i in range(n)]
for p in [1, 2, 3, -1]:
    if p == -1:
        print(max(D))
    else:
        print(math.pow(sum([math.pow(D[i],p) for i in range(n)]),1/p))

