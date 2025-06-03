N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = [_ for _ in input()]
cnt = 0
for i in range(N):
    if i < K or T[i] != T[i-K]:
        if T[i] == "r":
            cnt += P
        elif T[i] == "s":
            cnt += R
        else:
            cnt += S
    else:
        T[i] = "z"
print(cnt)