N = int(input())

ans = [0] * (N+1)

for i in range(N+1):
    if i % 3 != 0 and i % 5 != 0 and i % 15 != 0:
        ans[i] = ans[i-1] + i
    else:
        ans[i] = ans[i-1]
print(ans[-1])
