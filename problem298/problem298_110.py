N,K=map(int,input().split())
H=[int(h) for h in input().split()]
H=sorted(H)
cnt=0
for i in range(1,len(H)+1):
    if H[-i]>=K:
        cnt+=1
    else:
        print(cnt)
        exit()
print(cnt)
