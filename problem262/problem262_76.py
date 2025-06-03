N = int(input())

memberlist = []
testinomylist = []


for _ in range(N):

    A = int(input())
    tmpmemberlist = []
    tmptestinomylist = []
    
    for i in range(A):
        x, y = map(int, input().split())
        tmpmemberlist.append(x)
        tmptestinomylist.append(y)

    memberlist.append(tmpmemberlist)      # [[2,3],[1,3],[1]] こんな感じで人が収容
    testinomylist.append(tmptestinomylist) # [[0,1],[1],[0]]
        
ans = 0

for i in range(2 ** N):
    honestlist = []
    liarlist = []

    for j in range(N):  
        if ((i >> j) & 1):
            #if true 条件を満たした人を正直物として考える.
            honestlist.append(j+1)
        else:
            # if false の人は嘘つきものだと考える。
            liarlist.append(j+1)

    #正直な人だけを見ればいい。
    Flag = 0

    for honestnumber in honestlist: #bit全探索で得た正直な人の番号

        for X,Y in zip(memberlist[honestnumber-1] , testinomylist[honestnumber-1]): # 正直な人だけの証言
            if (Y == 0):
                if X in liarlist: #正直者の証言が食い違ってないか
                    pass
                else:
                    Flag = 1 
            elif (Y == 1):
                if X in honestlist:
                    pass
                else:
                    Flag = 1


    if Flag == 1:
        pass
    else:
        ans = max(ans,len(honestlist))

print(ans)
        
