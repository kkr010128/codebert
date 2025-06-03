N=int(input())

def num_divisors_table(n):
    table=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            table[j]+=1
    return table

l=num_divisors_table(N)
ans=0

for i in range(1,N+1):
    ans+=i*l[i]

print(ans)