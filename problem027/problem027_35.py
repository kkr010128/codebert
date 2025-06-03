def rec(A,n):
    if n==0:
        return A
    else:
        return rec(draw(A),n-1)

def draw(A):
    l=[]
    for i in range(len(A)-1):
        a=(A[i+1][0]-A[i][0])/3
        b=(A[i+1][1]-A[i][1])/3
        u0=(a,b)
        u60=(a*(1/2)-b*(3**(1/2)/2),a*(3**(1/2)/2)+b*(1/2))
        u300=(a*(1/2)+b*(3**(1/2)/2),-a*(3**(1/2)/2)+b*(1/2))
        
        P=(A[i][0]+u0[0],A[i][1]+u0[1])
        Q=(P[0]+u60[0],P[1]+u60[1])
        R=(Q[0]+u300[0],Q[1]+u300[1])

        l.extend([A[i],P,Q,R])
    l.append(A[-1])   
    return l

n=int(input())
A=[(0.0,0.0),(100.0,0.0)]
B=rec(A,n)

for P in B:
    print(f'{P[0]} {P[1]}')
