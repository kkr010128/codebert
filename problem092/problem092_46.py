import math
X,K,D=map(int,input().split())
count=0
#Xが初期値
#Dが移動量（+or-）
#K回移動後の最小の座標
#X/D＞Kの場合、K*D＋Xが答え

Y = 0
#X>0 D>0 の場合
if X / D > K and X / D > 0:
    Y = abs(X - D * K)
elif abs(X / D) > K and X / D < 0:
    Y = abs(X + D * K)
else:
    #X/D<Kの場合、X mod D
    L = abs(X) % D
    M = math.floor(abs(X) / D)
    if (K - M) % 2 == 0:
        Y = L
    else:
        Y=abs(L-D)

print(Y)