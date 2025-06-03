n=int(input())
G=[[0,[],0,-1]]
for i in range(n):
    v=[int(j) for j in input().split(" ")]
    u=v.pop(0)
    k=v.pop(0)
    G.append([k,v,0,-1])





distance=0
dis_list=[1]
G[1][3]=0
G[1][2]=1
while len(dis_list)!=0:
    distance+=1
    dis_list_cash=[]
    for i in dis_list:
        k=G[i][0]
        v=G[i][1]
        for j in range(k):
            if G[v[j]][2]==0:
                G[v[j]][2]=1
                G[v[j]][3]=distance
                dis_list_cash.append(v[j])
    
    dis_list=dis_list_cash



for i in range(1,n+1):
    print(str(i)+" "+str(G[i][3]))