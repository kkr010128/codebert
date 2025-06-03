N = int(input())
S = list(input())

R_list = [0]*N
G_list = [0]*N
B_list = [0]*N

for key,val in enumerate(S):
    if val=='R':
        R_list[key] = R_list[key-1]+1
        G_list[key] = G_list[key-1]
        B_list[key] = B_list[key-1]
    elif val=='G':
        R_list[key] = R_list[key-1]
        G_list[key] = G_list[key-1]+1
        B_list[key] = B_list[key-1]
    elif val=='B':
        R_list[key] = R_list[key-1]
        G_list[key] = G_list[key-1]
        B_list[key] = B_list[key-1]+1

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        if S[i]==S[j]:
            continue
        a=2*(j+1)-(i+1)-1
        check = [S[i],S[j]]
        if 'R' not in check:
            ans += R_list[-1]-R_list[j]
            if a<N and S[a]=='R':
                ans -= 1
        elif 'G' not in check:
            ans += G_list[-1]-G_list[j]
            if a<N and S[a]=='G':
                ans -= 1
        elif 'B' not in check:
            ans += B_list[-1]-B_list[j]
            if a<N and S[a]=='B':
                ans -= 1
print(ans)
