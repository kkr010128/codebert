import collections
n=int(input())
A=list(map(int,input().split()))

c = collections.Counter(A)
all_combi=0

for i in c:
    # print(c[i])
    all_combi +=  c[i]*(c[i]-1)//2

count = [c[A[i]] for i in range(len(A))]

for i in range(len(A)):
    

    n_same_i = count[i]-1 
    ans = all_combi - n_same_i
    
    print(ans)
        
