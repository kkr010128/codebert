import math


A, B, C = map(int, input().split())
K = int(input())

count = 0

ab = int(math.log2(A/B)+1)
bc = int(math.log2((B*(2**ab))/C)+1)

if ab + bc <= K:
    print('Yes')
else:
    print('No')
