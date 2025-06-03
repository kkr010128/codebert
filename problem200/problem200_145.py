a,b,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
for i in range(m):
    x,y,c = map(int, input().split())
    ans += [A[x-1] + B[y-1] - c]
ans += [min(A) + min(B)]

print(min(ans))