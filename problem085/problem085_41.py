from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

Ones = A.count(1)
R = max(A)
nums = [0]*(R+1)

# 素因数テーブルの作成
D = [0]*(R+1)
for i in range(2, R+1):
    if D[i]:
        continue
    n = i
    while n < R+1:
        if D[n] == 0:
            D[n] = i
        n += i

# 素因子をカウント
for a in A:
    tmp = a
    while tmp > 1:
        prime_factor = D[tmp]
        nums[prime_factor] += 1
        while tmp%prime_factor == 0:
            tmp //= prime_factor
y = max(nums)
if y < 2:
    print('pairwise coprime')
elif y-Ones < N:
    print('setwise coprime')
else:
    print('not coprime')