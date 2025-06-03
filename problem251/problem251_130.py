N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

li = [-1]*N #グー、チョキ、パー
se = set(["r","s","p"])
dic = {"r":"p","s":"r","p":"s"}
score = {"r":0,"s":0,"p":0}
#iはあまりでi+k*a
num = N//K
for i in range(K):
    for a in range(num+1):
        nex = i + K*a
        if nex>N-1:
            break 

        rival = T[nex]
        kati = dic[rival]
        
         
        if nex<K:
            li[nex]=kati
            score[kati]+=1
        elif not kati==li[nex-K]:
            li[nex]=kati
            score[kati]+=1
        #elif kati==li[nex-k]:
        # if nex+k>N-1:
        # else:
print(score["r"]*R+score["s"]*S+score["p"]*P)

