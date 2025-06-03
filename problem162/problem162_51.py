N,M=map(int,input().split())

x=list(range(1,N+1,1))

if N%2==1:
    for i in range(M):
        print(x.pop(0),x.pop(-1))
        
else:
    x_f=x[1:int(N/2+1)]
    x_l=x[int(N/2+1):]
    
    count=0
    
    for i in range(M):
        if len(x_f)>1:
            print(x_f.pop(0),x_f.pop(-1))
            count+=1
            
        if count==M:
            break
        
        if len(x_l)>1:
            print(x_l.pop(0),x_l.pop(-1))
            count+=1
            
        if count==M:
            break