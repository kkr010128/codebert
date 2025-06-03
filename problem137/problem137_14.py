# ABC169 E

N=int(input())
AB=[tuple(map(int,input().split())) for _ in [0]*N]

def med(A):
    N=len(A)
    if N%2:
        return A[(N+1)//2-1]
    else:
        return (A[N//2-1]+A[N//2])/2
    
A=[i[0] for i in AB]  
B=[i[1] for i in AB]
medA=med(sorted(A))
medB=med(sorted(B))

if N%2:
    print(medB-medA+1)
else:
    print(int(2*medB-2*medA+1))