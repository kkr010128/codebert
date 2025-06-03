from collections import Counter

def CHK():
    N = int(input())
    A = list(map(int,input().split()))
    L=[]
    R=[]
    cnt = 0
    for i in range(N):
        L.append(i + A[i])
    L_Cnt=Counter(L)

    for i in range(N):
        chk = i -A[i]
        cnt += L_Cnt[chk]
    print(cnt)

CHK()
