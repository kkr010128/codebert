# coding: utf-8
import sys
from collections import defaultdict

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# MODの管理をして右から進める
N, P = lr()
S = sr()
dic = defaultdict(int)
dic[0] = 1
num = 0
power = 1
answer = 0
if P%2 == 0 or P%5 == 0:
    x = [i for i, y in enumerate(S, 1) if int(y) % P == 0]
    answer = sum(x)
else:
    for s in S[::-1]:
        s = int(s)
        num += s * power
        num %= P
        answer += dic[num]
        dic[num] += 1
        power *= 10; power %= P

print(answer)
# 14