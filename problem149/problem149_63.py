import numpy as np

n, m, x = map(int, input().split())
data = []
for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
# ------------------------
# 今回の場合は、MとNが異様に小さいので、全探索して、Xを超える条件をMinで取るのがBetter
cost = 10 ** 17


# 0の場合は全部がOFFなので、はじく。
for bit in range(1, 2 ** n):
    # print(bit)
    ttt = np.zeros(m + 1)

    for j in range(n):
        # onの場合
        if (bit >> j & 1):
            #print('OK!', j)
            tar = np.array(data[j])
            ttt += tar

    check = np.where(ttt[1:] >= x)[0]
    if (len(check) == m):
        cost = min(cost, ttt[0])
    else:
        pass

if (cost == 10 ** 17):
    print(-1)
else:
    print(int(cost))
