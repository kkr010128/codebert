n = int(input())
adjMat = [[-1]*n for i in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        adjMat[i][x-1] = y
ans = 0
for i in range(1 << (n)):
    #print (bin(i))
    success = True
    for j in range(n):
        if i & 2**j:
            for k in range(n):
                if k == j:
                    continue
                if  i & 2**k == 0 and adjMat[j][k] == 1:
                    success = False
                if i & 2**k > 0 and adjMat[k][j] == 0:
                    success = False
                #print (j, k, adjMat[j][k], adjMat[k][j], success)
        if not success:
            break
    if success:
        i2 = i
        c = 0
        while i2 > 0:
            c += i2 & 1
            i2 //= 2
        ans = max(c, ans)
print (ans) 