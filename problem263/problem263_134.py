mod = 10**9 + 7
N = int(input())
A = [int(i) for i in input().split()]
# bitにしてor
# 一桁だけの時、111000なら3 * 3
maxl = 0
textlist = []
for i in range(N):
    tmp = str(bin(A[i]))
    tmp = tmp[2:]
    length = len(tmp)
    if maxl < length:
        maxl = length
    textlist.append(tmp)
zeros = {}
ones = {}
for i in range(maxl):
    zeros[i] = 0
    ones[i] = 0

for i in range(N):
    tmp = textlist[i]
    length = len(tmp)
    if maxl < length:
        maxl = length
    for j in range(length):
        if tmp[-j-1]== '1':
            ones[j] += 1
for i in range(maxl):
    zeros[i] = N-ones[i]

result = 0
n2 = 1
for i in range(maxl):
    result = (result + n2 * (zeros[i] * ones[i])) % mod
    n2  = (n2 * 2) % mod
print(result)