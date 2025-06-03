N,M = map(int,input().split())
ls2 = []
for i in range(M):
    ls1 = list(map(int,input().split()))
    ls2.append(ls1)

ans = -1
if M == 0:
    if N==1:
        ans = 0
    else:    
        ans = 10**(N-1)
if N == 1:
    for i in range(10):
        for j in range(M):
            if not i//(10**(N-ls2[j][0]))%10 == ls2[j][1]:
                break
            if j == M-1:
                ans = i
                break
        if not ans == -1:
            break   

else:
    for i in range(10**(N-1),10**N):
        for j in range(M):
            if not i//(10**(N-ls2[j][0]))%10 == ls2[j][1]:
                break
            if j == M-1:
                ans = i
                break
        if not ans == -1:
            break
print(ans)          
