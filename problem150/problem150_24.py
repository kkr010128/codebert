n,k = map(int,input().split()) 
A=list(map(int,input().split()) )

kyori = [-1] *len(A)

junban =[]

x=0
d=0
while kyori[x] == -1:
    
    junban.append(x)
    kyori[x]=d
    d+=1
    x=A[x]-1
    
    
roop_x = x
roop_d = d - kyori[x]

# for k in range(100):

if k<d:
    print(junban[k]+1)
    
else:
    
    k0 = kyori[x]
    k1 = (k-k0)%roop_d
    
    print(junban[k0+k1]+1)
