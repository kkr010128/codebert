import sys
import numpy as np
from collections import Counter
# 全探索なら、 2**6 * 2**6 （4000）
#            > 4000 * (6**2)
# bit全探索でOK
# ------------------------------------------
h, w, num = map(int, input().split())
data = []
for _ in range(h):
    # 一文字ずつListへ格納
    temp = list(input())
    data.append(temp)
#data = [input() for _ in range(h)]
# print(data)

'''
count = Counter(data)
most = count.most_common()
print(most)
'''
ans = 0

# 縦の全Loop
for i in range(2 ** h):
    for j in range(2 ** w):
        #print(i, j)
        *temp, = data
        temp = np.array(temp)
        for k in range(h):
            if (i >> k & 1):
                temp[k, :] = 'aa'

        for l in range(w):
            if (j >> l & 1):
                temp[:, l] = 'aa'

        count = np.where(temp == '#')[0]
        #print(count, len(count))
        if (len(count) == num):
            # print('add')
            ans += 1
        else:
            pass


print(ans)
