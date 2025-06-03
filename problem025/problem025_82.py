n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

ans = [0] * (2 ** n)
for i in range(2 ** n):
    p = 1
    for j in range(n):
        if i & p:
            ans[i] += A[j]
        p *= 2

for i in range(q):
    if m[i] in ans:
        print("yes")
    else:
        print("no")

