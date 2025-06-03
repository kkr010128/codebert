N = int(input())
A = map(int, input().split())
B = [3 if i == 0 else 0 for i in range(N + 1)]
MOD = 1000000007
ans = 1
for a in A:
    ans = ans * B[a] % MOD
    if ans == 0:
        break
    else:
        B[a] -= 1
        B[a + 1] += 1
print(ans)
