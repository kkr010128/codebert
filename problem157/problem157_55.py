N = int(input())
*A, = map(int, input().split())
dic = {}
ans = 0
for i in range(N):
    if A[i] + i in dic:
        dic[A[i] + i] += 1
    if A[i] + i not in dic:
        dic[A[i] + i] = 1
    if i - A[i] in dic:
        ans += dic[i - A[i]]
print(ans)