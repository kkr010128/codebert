import math

N, K = map(int,input().split())
A = list(map(int,input().split()))

L = 1
R = 10**9+1
ans = float("INF")

while True: # midの長さの丸太に切るとして2分探索
    mid = (L + R) // 2
    cur = 0
    for i in range(N):
        cur += math.ceil(A[i]/mid) - 1 # 切る必要回数
    
    if cur > K: #K回より大きい時は、L=midとして長くする 
        if L == mid:
            break
        L = mid
    else: #K回以下の時は、R=midとして短くする 
        ans = min(ans, mid)
        if R == mid:
            break
        R = mid
        
print(ans)