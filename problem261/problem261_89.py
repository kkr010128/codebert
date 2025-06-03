S = input() 
N=len(S)
h=0
for i in range(0,N//2):
    if S[i]!=S[N-1-i]:
            h+=1
print(h)