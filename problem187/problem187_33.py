N,X,Y = list(map(int,input().split()))

ans_dict={}
for n in range(1,N):
    ans_dict[n]=0
    
for n1 in range(1,N+1):
    for n2 in range(n1+1,N+1):
        ans_1 = abs(n1-n2)
        ans_2 = abs(n1-X)+abs(n2-Y)+1
        ans_3 = abs(n2-X)+abs(n1-Y)+1
        
        ans=min(ans_1,ans_2,ans_3)
        ans_dict[ans]+=1
        

for k in ans_dict.keys():
    print(ans_dict[k])