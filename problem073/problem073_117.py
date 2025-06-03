N = int(input())
L = [0]*(N)
for i in range(1,N):
    for j in range(1,(N-1)//i+1):
        L[j*i]+=1
print(sum(L))