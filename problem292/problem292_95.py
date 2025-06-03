n = int(input())
#a, b = map(int, input().split())
l = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        if i < j:
            ans = ans + l[i] * l[j]
print(ans)


