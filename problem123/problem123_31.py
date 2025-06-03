n = int(input())
A = list(map(int,input().split()))

xor_sum = 0
for i in range(n):
    xor_sum = xor_sum^A[i]

ans = []
for i in range(n):
    ans.append(xor_sum^A[i])
print(' '.join(map(str,ans)))
