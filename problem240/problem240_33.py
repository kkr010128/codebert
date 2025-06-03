#C - Welcome to AtCoder
N,M = map(int,input().split())
S_P_list = []
for _ in range(M):
    p,s = input().split()
    S_P_list.append((int(p),s))
#Pに着目して安定ソート
S_P_list = sorted(S_P_list,key = lambda x:x[0],reverse = False)    
#ACが存在するPの集合
AC_list = list(set([i[0] for i in S_P_list if i[1] == 'AC']))
WA = 0
AC = 0
for i in range(M):
    if (S_P_list[i][0] in AC_list):
        if S_P_list[i][1] == 'AC':
            AC += 1
            AC_list.remove(S_P_list[i][0])
        else:
            WA += 1
print(AC,WA)