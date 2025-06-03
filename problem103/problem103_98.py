# 7
# 100 130 130 130 115 115 150
import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))
m = 1000
kabu = 0
buy = True
buy_val = 100000

for i in range(len(a)):
    if i == len(a)-1:
        m += kabu * a[i]
        kabu = 0

    elif not buy and a[i] > a[i+1]:
        m += kabu * a[i]
        kabu=0
        buy=True
    elif buy and a[i] < a[i+1]:
        kabu=int(m/a[i])
        m -= kabu * a[i]
        buy=False

print(m)
