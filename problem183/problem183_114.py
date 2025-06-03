N = int(input())

divisor = [N]
ans = 0

#Nの約数の列挙
for i in range(2,N+1,1):
    if i*i < N:
        if N % i == 0:
            divisor.append(i)
            divisor.append(N//i)
    elif i*i == N:
        divisor.append(i)
    else:
        break

#N-1の約数の列挙
yakusuuu = [N-1]
for i in range(2,N,1):
    if i*i < (N-1):
        if (N - 1)% i == 0:
            yakusuuu.append(i)
            yakusuuu.append((N-1)//i)
    elif i*i == (N-1):
        yakusuuu.append(i)
    else:
        break

for i in yakusuuu:
    if N % i == 1:
        ans += 1

#print(divisor)
#print(yakusuuu)

M = N

for K in divisor:
    #print(K)
    while M % K == 0:
        M = M//K

    

    if M == 1:
        ans += 1
        
    else:
        M =  M % K
        if M == 1:
            ans += 1 
    
    M = N
        




print(ans)