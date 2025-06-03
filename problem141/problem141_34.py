import math

N = int(input())
# A = list(map(int, input().split()))
A = [int(x) for x in input().split(' ')]


a_max = [0] * (N+1)
a_min = [0] * (N+1)
a = [0] * (N+1)

#１．可・不可の判定
# 最下段からとりうる個数の範囲を考える
#0段目の範囲に１が含まれないならば”不可”(根＝１)

for i in range(N+1):
    if i == 0:
        a_max[N-i] = A[N-i]
        a_min[N-i] = A[N-i]
    else:
        a_max[N-i] = a_max[N-i+1] + A[N-i]
        a_min[N-i] = math.ceil(a_min[N-i+1]/2) + A[N-i]

#check print
# for i in range(N+1):
#     print(str(i) + ':----')
#     print(a_min[i],a_max[i])

#最上段から個数のカウント
for i in range(N+1):
    if i == 0:
        a[i] = 1
    else:
        a[i] = min((a[i-1] - A[i-1])*2 , a_max[i])

#不可は-1を、可は個数の合計を
if a_min[0] > 1:
    print(-1)
else:
    print(sum(a))
