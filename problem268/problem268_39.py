N = int(input())
a = [int(x) for x in input().split()]
MOD = 10**9 + 7
ans = 1

lst = [0] * 3

for aa in a:
    cnt = 0
    j = -1
    for i, l in enumerate(lst):
        if l == aa:
            cnt += 1
            j = i
    if j == -1:
        ans = 0
        break
    ans *= cnt
    ans %= MOD
    lst[j] += 1

print(ans)