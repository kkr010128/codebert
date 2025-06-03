N, K = map(int, input().split())
A = list(map(int, input().split()))
B = []
T = {"mi":0, "pu":0, "zero":0}

for i in range(N):
    if A[i] < 0:
        T["mi"] += 1
    elif A[i] == 0:
        T["zero"] += 1
    else:
        T["pu"] += 1
mod = 10**9+7
for i in range(N):
    if A[i] < 0:
        B.append([A[i]*(-1), 1])
    else:
        B.append([A[i], 0])
A.sort()
B.sort(reverse=True)

ans = 1
c = 0
for i in range(K):
    ans *= B[i][0]
    ans %= mod
    c += B[i][1]

if c % 2 == 0:
    print(ans)
elif K > T["pu"]+T["mi"]:
    print(0)
elif T["mi"] == 1 and K > T["pu"]:
    ans = 1
    for i in range(N):
        ans *= A[i]
        ans %= mod
    if T["zero"] != 0:
        ans = 0
    print(ans)
elif T["pu"] == 1 and K > T["mi"]:
    ans = 1
    for i in range(N):
        ans *= A[i]
        ans %= mod
    if T["zero"] != 0:
        ans = 0
    print(ans)
elif T["pu"] == 0:
    ans = 1
    A.reverse()
    for i in range(K):
        ans *= A[i]
        ans %= mod
    if T["zero"] != 0:
        ans = 0
    print(ans)
elif N == K:
    ans = 1
    for i in range(N):
        ans *= A[i]
        ans %= mod
    print(ans)
else:
    change1 = B[K-1][1]
    change2 = (change1 + 1)%2
    chindex1 = K-1
    chindex2 = -1
    for i in range(K-1, -1, -1):
        if B[i][1] == change2:
            chindex2 = i
            break
    afterindex1 = -1
    afterindex2 = -1
    for i in range(K, N):
        if B[i][1] == change2:
            afterindex1 = i
            break
    for i in range(K, N):
        if B[i][1] == change1:
            afterindex2 = i
            break
    result1 = 0
    result2 = 0
    if chindex1 >= 0 and afterindex1 >= 0:
        ans = 1
        for i in range(N):
            if i <= K-1 or i == afterindex1:
                if i != chindex1:
                    ans *= B[i][0]
                    ans %= mod
        result1 = ans
    if chindex2 >= 0 and afterindex2 >= 0:
        ans = 1
        for i in range(N):
            if i <= K-1 or i == afterindex2:
                if i != chindex2:
                    ans *= B[i][0]
                    ans %= mod
        result2 = ans
    if result1 == 0 and result2 == 0:
        print(0)
    elif result1 == 0:
        print(result2)
    elif result2 == 0:
        print(result1)
    elif B[afterindex1][0]*B[chindex2][0] - B[afterindex2][0]*B[chindex1][0] > 0:
        print(result1)
    else:
        print(result2)