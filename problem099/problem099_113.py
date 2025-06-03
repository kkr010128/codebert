#E - Logs
import math
# 入力
N,K = map(int,input().split())
A   = list(map(int,input().split()))
Amax = int(max(A))
high = Amax
Cancut = Amax
low  = 0
while ( (high - low) > 0.01 ) :
    Cut = 0
    X = (high + low) / 2.0
    for i in range(N):
        Cut = Cut + math.ceil(A[i]/X) - 1
    if Cut <= K:
        high = X
        Cancut = X
    else:
        low  = X
# 出力
if (math.floor(high) != math.floor(low)):
    Cancut = math.floor( 100 * Cancut) /100.0
print(math.ceil(Cancut))