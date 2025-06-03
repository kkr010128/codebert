S=list(input())
T=list(input())
A=[]
for i in range(len(S)-len(T)+1):
    B=0
    for j in range(len(T)):
        if T[j]==S[i+j]:
            continue
        else:
            B =B+1
    A.append(B)

A.sort()
print(A[0])

