N = int(input())
ll = [] #リストのリスト
for i in range(N):
    l = [None]*N
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        l[x-1] = y
    ll.append(l)

ans = 0
for i in range(1, 2**N): #bit全探索
    b = 1
    hon = [0]*N #正直者なら1, 
    for j in range(N):
        if i>>j&1:
            hon[j] = 1
    
    for k in range(N): # llとhonの比較 # 全正直者について
        if hon[k]==1: #正直者のつじつまを合わせる
            for h in range(len(ll[k])): #正直者の全ての証言について	
                if ll[k][h]==None:
                    continue
                if hon[h]!=ll[k][h]:
                    b = 0
                
   
    if b:
        p = hon.count(1)
        ans = max(p, ans)
print(ans)