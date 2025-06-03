N=int(input())
S=list(input())
a=0
for i in range(0,N-2):
    if (S[i]+S[i+1]+S[i+2])=='ABC':
        a+=1
print(a)