import sys
input = sys.stdin.readline

n,k = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9 + 7

# from random import randint
# n = 10
# k = 4
# A = []
# for i in range(10):
#     A.append(randint(-20,20))
# anss=0
# for i in range(n):
#     for j in range(i+1,n):
#         for ii in range(j+1,n):
#             for jj in range(ii+1,n):
#                 anss = max(anss, A[i]*A[j]*A[ii]*A[jj])
# print(anss)
# print(A)


B = [[], []]
for i in range(n):
    if A[i] >= 0:
        B[0].append(A[i])
    else:
        B[1].append(A[i])
B[0].sort(reverse=True)
B[1].sort()

if k % 2 == 1 and len(B[0]) == 0:
    ans = 1
    ind = len(B[1])-1
    for i in range(k):
        ans = (ans * B[1][ind]) % mod
        ind -= 1
    print(ans)
elif k == n and len(B[1]) % 2 == 1:
    ans = 1
    for i in range(n):
        ans = (ans * A[i]) % mod
    print(ans)
else:
    k0 = min(len(B[0]), k)
    k1 = k-k0
    if k1%2==1:
        k0 -= 1
        k1 += 1
    # print(B,k0,k1)
    while k1+1 < len(B[1]) and k0-2 >= 0 and B[1][k1]*B[1][k1+1] > B[0][k0-1]*B[0][k0-2]:
        k1 += 2
        k0 -= 2
        # print(k0,k1)
        # print(k1+1 < len(B[1]),B[1][k1]*B[1][k1+1] , B[0][k0-1]*B[0][k0-2])
    ans = 1
    for i in range(k0):
        ans = (ans * B[0][i]) % mod
    for i in range(k1):
        ans = (ans * B[1][i]) % mod
    print(ans)

