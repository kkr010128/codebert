# coding: utf-8

N,P = list(map(int, input().split()))
S = '0'+input()

#N=200000
#P=9893
#S= '0'+'1234567890' * 20000

if (P==2)|(P==5):
    sum=0
    for i in range(N, 0, -1):
        if int(S[i]) % P == 0:
            sum+= i
    print(sum)


else:
    dp1 = [0] * (N+1)
    dp2 = [0] * (N+1)
    dp3 = [0] * P
    dp1[N] = int(S[N]) % P
    dp3[int(dp1[N])] += 1
    k = 1
    for i in range(N - 1, 0, -1):
        dp1[i] = (dp1[i + 1] + (int(S[i]) * 10 * k)) % P
        dp3[int(dp1[i])] += 1
        k = (k * 10) % P

    sum = 0

    for i in range(P):
        if i == 0:
            sum += (dp3[i] * (dp3[i] - 1)) // 2 + dp3[i]
            continue
        if dp3[i] == 0: continue
        sum += (dp3[i] * (dp3[i] - 1)) // 2
    print(int(sum))
