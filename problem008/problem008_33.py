cnt = 1
def dep(G,s_cnt,f_cnt,np):
    global cnt
    s_cnt[np] = cnt
    cnt += 1
    for i in range(n):
        if G[np][i] == 1 and s_cnt[i] == 0:
            dep(G,s_cnt,f_cnt,i)
    f_cnt[np] = cnt
    cnt += 1
    

n = int(input())
G = [[0 for i in range(n)] for j in range(n)]
s_cnt = [0 for i in range(n)]
f_cnt = [0 for i in range(n)]

for i in range(n):
    S = list(map(int, input().split()))
    tmp_n = S[1]
    for j in range(tmp_n):
        G[i][S[j+2]-1] = 1
        
for i in range(n):
    if s_cnt[i]==0:
        dep(G,s_cnt,f_cnt,i)

for i in range(n):
    print(i+1,s_cnt[i],f_cnt[i])
