N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()
V = {"s":R, "p":S, "r":P}
ans = 0
for i in range(K):
    check = T[i]
    ans += V[T[i]]
    while True:
        i += K
        if i >= N:
            break
        if check == T[i]:
            check = -1
        else:
            ans += V[T[i]]
            check = T[i]
print(ans)