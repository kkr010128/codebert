n = int(input())
a = list(map(int,input().split()))
A = 0
for i in range(n):
    A ^= a[i]
ans = []
for i in range(n):
    ans.append(A^a[i])
print(" ".join(map(str,ans)))