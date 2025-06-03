#!/usr/bin/env python3

n = int(input())
x = input()
b = [0] * (n+1)
for i in range(1, n+1):
    bit_count = 0
    for j in range(20):
        if i >> j & 1:
            bit_count += 1
    b[i] = bit_count

popcount = [0] * (n+1)
cnt = x.count('1')
for i in range(1, n+1):
    popcount[i] = popcount[i % b[i]] + 1

ans = []
if cnt == 1:
    tmp = 0
    for i in range(n):
        if x[i] == '1':
            tmp += pow(2, n-i-1, 2)
            tmp %= 2
    for i in range(n):
        if x[i] == '1':
            ans.append(0)
        else:
            ans.append(popcount[(tmp - pow(2, n-i-1, 2)) % 2] + 1)
else:
    tmp1 = 0
    tmp2 = 0
    for i in range(n):
        if x[i] == '1':
            tmp1 += pow(2, n-i-1, cnt + 1)
            tmp2 += pow(2, n-i-1, cnt - 1)
    for i in range(n):
        if x[i] == '1':
            ans.append(popcount[(tmp2 - pow(2, n-i-1, cnt - 1)) % (cnt - 1)] + 1)
        else:
            ans.append(popcount[(tmp1 + pow(2, n-i-1, cnt + 1)) % (cnt + 1)] + 1)

for i in ans:
    print(i)