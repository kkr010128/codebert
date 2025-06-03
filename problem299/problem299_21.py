n = int(input())
a = list(map(int, input().split()))

ans = [""]*n

for i in range(n):
    x = a[i]
    b = ans[a[i] - 1]
    c = str(i+1)
    ans[a[i]-1] = str(i+1)

print(" ".join(ans))