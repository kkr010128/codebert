import numpy as np

n = int(input())
A, B = [], []  # AにはXがとりうる値の最小値、Bには最大値を入れていく

for _ in range(n):
    a, b = map(int, input().split())
    A.append(a if n % 2 == 1 else a * 2)  # nが偶数だと、medianがとりうる値が0.5刻みになるので最初から2倍にしておく
    B.append(b if n % 2 == 1 else b * 2)

a = np.median(A)
b = np.median(B)

# medianのとりうる値の最小値と最大値の間に、カウントしたいmedianが１刻みで存在する
print(int(max(a, b) - min(a, b) + 1))