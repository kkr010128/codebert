N=int(input())
S=str(input())
ans = S.count("R")*S.count("G")*S.count("B")
#print(ans)
for i in range(N-2):
    for j in range(i+1,N-1):
        k = 2*j-i
        #print(i,j,k)
        if k <= N-1:
            if S[i]!=S[j] and S[i]!=S[k] and S[j]!=S[k]:
                ans -= 1
print(ans)
