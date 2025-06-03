import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k = map(int, input().split())
M = 10**9+7
nums = [0]*(k+1) # gcd==kなる数列の個数
for i in range(k, 0, -1):
    nums[i] = pow(k//i, n, M)
    for j in range(2*i, k+1, i):
        nums[i] -= nums[j]
    nums[i] %= M
ans = sum(i*item for i,item in enumerate(nums))%M
print(ans)