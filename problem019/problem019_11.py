from queue import Queue

n,q =map(int,input().split()) ##n:プロセス数、q:クオンタム

qu=Queue()  ##意味を調べる

for i in range(n):
    name,t=input().split()
    qu.put((name,int(t))) ##Queueのput?
    

cnt=0

while qu.qsize()>0: ##qsize?
    name,t=qu.get() 
    cnt+=min(q,t)  ##処理時間と残り時間の小さい方をたす
    if q< t:
        qu.put((name,t-q))  ##残り時間から処理時間を引いて、後ろに回す
    else:
        print(name,cnt)

