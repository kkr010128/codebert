
N = int(input())
S = [x for x in input()]
Q = int(input())

#A1 ... AnのBIT(1-indexed)
BIT = [[0] * (N + 1) for _ in range(26)]

#A1 ~ Aiまでの和 O(logN)
def BIT_query(input_BIT, idx):
    res_sum = 0
    while idx > 0:
        res_sum += input_BIT[idx]
        idx -= idx&(-idx)
    return res_sum

#Ai += x O(logN)
def BIT_update(input_BIT,idx,x):
    while idx <= N:
        input_BIT[idx] += x
        idx += (idx&(-idx))
    return

for i, c in enumerate(S):
    BIT_update(BIT[ord(c)-ord('a')], i+1, 1)
  
for _ in range(Q):
    a, b, c = input().rstrip().split()
    if int(a) == 1:
        BIT_update(BIT[ord(S[int(b)-1])-ord('a')], int(b), -1)
        BIT_update(BIT[ord(c)-ord('a')], int(b), 1)
        S[int(b)-1] = c
    else:
        count = 0
        for i in range(26):
            if BIT_query(BIT[i], int(b)-1) != BIT_query(BIT[i], int(c)):
                count += 1
        print(count)