import math
X, K, D = map(int, input().split())

kyori = abs(X)
kaisu = math.ceil(kyori / D)

if(K < kaisu):
    ans = kyori - (K * D)
    #if(X < 0):
    #    print(-ans)
    #else:
    #    print(ans)
else:
    if((K - kaisu) % 2 == 0):
        ans = kyori - (kaisu * D)
    else:
        ans = kyori - (kaisu * D) + D

    #if(X < 0):
    #    print(-ans)
    #else:
    #    print(ans)

print(abs(ans))