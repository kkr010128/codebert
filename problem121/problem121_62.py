from collections import deque  # dequeはappendleftができるので。

letter = ['z'] + [chr(i) for i in range(97, 123)]  # [0, a, b, c, ... , z]というリスト

N = int(input())

i = 0
n_24 = deque()

while N > 0:
    n_24.appendleft(N % 26)
    if N%26== 0:
        N -= 26
    N = N // 26

ans = ''

for dig in (n_24):
    ans += letter[dig]

print(ans)