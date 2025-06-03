## coding: UTF-8

N, P = map(int,input().split())
S = input()[::-1]


remainder = [0] * P
tmp = 0
rad = 1 #10**(i) % P

'''
if(P == 2 or P == 5):
    for i in range(N):
        r = int(S[i])
        tmp += r * rad
        tmp %= P
        remainder[tmp] += 1
        rad *= 10
'''
if(P == 2):
    ans = 0
    for i in range(N):
        r = int(S[i])
        if(r % 2 == 0):
            ans += N-i
    print(ans)
elif(P == 5):
    ans = 0
    for i in range(N):
        r = int(S[i])
        if(r % 5 == 0):
            ans += N-i
    print(ans)
else:
    for i in range(N):
        r = int(S[i])
        tmp += r * rad
        tmp %= P
        remainder[tmp] += 1
        rad *= 10
        rad %= P
    remainder[0] += 1

    #print(remainder)

    ans = 0
    for i in range(P):
        e = remainder[i]
        ans += e*(e-1)/2
    print(int(ans))

