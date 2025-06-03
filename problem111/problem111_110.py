'''
参考
https://yamakasa.net/atcoder-abc-173-d/
図
https://github.com/ymo999/AtCoder/blob/master/2020/20200705_ABC173/ABC173_D.pdf
'''
import math

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 0
for i in range(1, N):
    idx = math.floor(i/2)           # 心地よさの和を算出するためのindex
    ans += A[idx]

print(ans)
