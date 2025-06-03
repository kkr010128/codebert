S= input()
T=input()
mi = 3000
for i in range(0,len(S)-len(T)+1):
    c = 0
    for j in range(0,len(T)):
        #print(S[i+j]+":"+T[j])
        
        if S[i+j] != T[j]:
            c += 1

        #print(c)
    if mi > c:
        mi = c
print(mi)