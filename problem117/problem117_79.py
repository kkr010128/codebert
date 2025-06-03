N,M,K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

###Bをi冊目まで読むのにどれだけ時間がかかるか
P = [0]*M
P[0] = B[0]
for i in range(1,M):
    P[i] = P[i-1] + B[i]

T = K###残り時間
ans = 0
num = M-1
for i in range(N):
    T -= A[i]
    if T < 0:
        break
    while P[num] > T and num >= 0:
        num -= 1
    ans = max(ans,i+num+2)
    #print(i,num,ans)

###Aを1冊も読まない場合
for i in range(M):
    if P[i] <= K:
        ans = max(ans,i+1)
    else:
        break

print(ans)