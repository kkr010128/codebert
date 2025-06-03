S=input()
T=input()

N = len(S)

count = 0
for n in range(N):
    if S[n]!=T[n]:
        count+=1
print(count)
