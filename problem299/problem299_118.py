n = int(input())
a = list(map(int, input().split()))
a_to_index = [0] * n
for i in range(n):
    a_to_index[a[i]-1] = i + 1
a.sort()
ans = [0] * n
for index, ai in enumerate(a):
    ans[index] = a_to_index[ai-1]
print(*ans)
