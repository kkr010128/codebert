#177B

S=input()
T=input()

Ss=[]
Ts=[]
Us=[]
Vs=[]

len_T=len(T)
len_S=len(S)

s=0

#初期配列を作成
for t in range(len_T):
    Ts.append(T[t])
    Ss.append(S[t])

#一致していない箇所の個数を数え、記録
for t in range(len_T):
    Us.append(Ts[t]!=Ss[t])
Vs.append(sum(Us))


for s in range(1,len_S-len_T+1):
    #Ss配列をずらす
    Ss.append(S[len_T+s-1])
    Ss.remove(S[s-1])
    #Usをリセットして、一致していない箇所の個数を数え、記録
    Us=[]
    for t in range(len(T)):
        Us.append(Ts[t]!=Ss[t])
    Vs.append(sum(Us))
    
print(str(min(Vs)))

