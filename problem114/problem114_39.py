D = int(input())
C = list(map(int,input().split())) #C[i]AiCを実施しないと下がる満足度
S = [] #S[i][j] i日目にAjcというコンテストを実施した場合に上がる満足度
for i in range(D): #コンテストは0index
    temp = list(map(int,input().split()))
    S.append(temp)
T = []
for i in range(D):
    temp = int(input())
    T.append(temp)
since = [0 for _ in range(26)] #最後に開催されてから何日経ったか。
manzoku = 0
for i in range(26):
    since[i] += C[i]
for i in range(D):
    contest = T[i]-1 #0index
    manzoku += S[i][contest]
    for j in range(26):
        if j != contest:
            manzoku -= since[j]
    print(manzoku)
    for j in range(26):
        if j != contest:
            since[j] += C[j]
        else:
            since[j] = C[j]    