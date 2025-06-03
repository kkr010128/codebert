N, P = map(int, input().split())
S = list(map(int, input()))
ans = 0
if P == 2:
    for i in range(N):
        if S[i]%2 == 0:
            ans +=i+1
    print(ans)

elif P ==5:
    for i in range(N):
        if S[i]%5 == 0:
            ans +=i+1
    print(ans)
else:
    data =[0]*P
    tens = 1
    k = 0
    for i in range(N-1,-1,-1):
        k += S[i] *tens %P
        k = k%P
        data[k] += 1
        tens *=10
        tens %=P

    for i in data:
        ans += i*(i-1)/2
    ans +=data[0]
    print(int(ans))