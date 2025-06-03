##未完成

N = int(input())
K = str(N)
l = len(str(N))

ans = 0

def tp(i,j,p):
    tmp = 0
    if p >= 2:
        if l == p:
            if i == int(K[0]):
                if j > int(K[l-1]):
                    tmp = (N-int(K[0])*10**(l-1)-int(K[l-1]))//10
                else:
                    tmp = (N-int(K[0])*10**(l-1)-int(K[l-1]))//10+1
            elif i >= int(K[0]):
                tmp = 0
            else:
                tmp = 10**(p-2)
        elif l > p:
            tmp = 10**(p-2)
        return tmp
    else:
        if i == j and i <= N:
            return 1
        else:
            return 0


for i in range(1,10):
    for j in range(1,10):
        for p in range(1,l+1):
            for q in range(1,l+1):
                ans += tp(i,j,p)*tp(j,i,q)

print(ans)