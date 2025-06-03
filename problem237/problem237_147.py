# 多次元リストの sort に使える
from operator import itemgetter

n = int(input())
x = [0] * n
l = [0] * n
for i in range(n):
    x[i], l[i] = map(int, input().split())

st = sorted([(x[i] - l[i], x[i] + l[i]) for i in range(n)], key = itemgetter(1))

ans = 0
# 最後に選んだ仕事の終了時間
last = - 10 ** 10

for i in range(n):
    if last <= st[i][0]:
        ans += 1
        last = st[i][1]

print(ans)