N,M=map(int,input().split())
S,r,s=input(),[],N
for _ in range(2*N):
    if S[s]=='1':
        s += 1
    else:
        r.append(str(N-s))
        N,s=s,max(0,s-M)
    if N == 0:
        break
print(*[-1] if s else r[1:][::-1])