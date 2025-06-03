N = int(input())

C=[[0]*10 for _ in range(10)]

for n in range(1,N+1):
    n=str(n)
    n_s=int(n[0])
    n_e=int(n[-1])
    
    C[n_s][n_e]+=1
    
ans=0
for c_1 in range(10):
    for c_2 in range(10):
        ans += C[c_1][c_2]*C[c_2][c_1]
        
print(ans)