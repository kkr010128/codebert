N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7
# N = 6
# A = [0, 1, 0, 0, 1, 2]

xyz = [[0]*(N+1) for _ in range(3)]
for i in range(N):
    is_added = False
    for j in range(3):
        if xyz[j][i] == A[i] and not is_added:
            xyz[j][i+1] = xyz[j][i] + 1
            is_added = True
        else:
            xyz[j][i+1] = xyz[j][i]

# for i in range(3):
#     print(xyz[i])

ans = 1
for i in range(N):
    cnt = 0
    for j in range(3):
        if xyz[j][i] == A[i]:
            cnt += 1
    ans = ans*cnt % MOD
print(ans)
