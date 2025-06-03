n,t=[int(x) for x in input().split()]
w=[]
for i in range(n):
    w.append(int(input()))

totalw=sum(w)  
pmax=totalw
pmin=int(totalw/t)-1

def check(ptest):
    tk=1
    p=0
    global t
    global w
    global n
    i=0
    
    while i<n:
        p+=w[i]
        if p<=ptest:
            i+=1
        else:
            tk+=1
            p=0
            
        if tk>t:
            return 0
            #break   
    
    return 1
    
        
while (pmax-pmin)>1:
    pmid=(pmax+pmin)//2
    if check(pmid)==1:
        pmax=pmid
    else:
        pmin=pmid
        
print(pmax)
