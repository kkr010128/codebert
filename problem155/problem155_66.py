n,m = map(int,input().split())
h = list(map(int,input().split()))
judge = [True] * n

for i in range(m):
    a,b = map(int,input().split())
    if h[a-1] == h[b-1]:
        judge[a-1],judge[b-1] =False, False
    elif h[a-1] > h[b-1]:
        judge[b-1] = False
    else:
        judge[a-1] = False

print(judge.count(True))
