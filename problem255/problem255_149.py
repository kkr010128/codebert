N = int(input())
S, T = map(str, input().split())

S = list(S)
T = list(T)
ANS = []

for i in range(N):
    ANS.append(S[i])
    ANS.append(T[i])
    
ANS = ''.join(ANS) 
    
    
print(ANS)