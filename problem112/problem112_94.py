import functools

def sign(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    else:
        return -1

def multiply(x,y):
    ans = x*y
    if ans>=10**9+7 or ans<0:
        ans %= (10**9+7)
    return ans

N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

if (A[-1]<0 and K%2==1):
    combi = A[-K:]
    if K >1:
        answer =  functools.reduce(multiply,combi)

elif K == N:
    answer = functools.reduce(multiply,A)

else:
    signs = 1
    i,j = 0,0
    for _ in range(K):
        if abs(A[i]) > abs(A[N-j-1]):
            signs *= sign(A[i])
            i += 1

        else:
            signs *= sign(A[N-j-1])
            j += 1
    combi = A[N-j:] + A[:i]
    del A[N-j:]
    del A[:i]
    combi = combi[::-1]

    if signs == -1:
        if A:
            if combi[-1]<0:
                del combi[0]
                combi.append(A[-1])
            elif A[0]>=0:
                del combi[0]
                combi.append(A[-1])
            elif A[0]<0 and A[-1] >0:
                if combi[0]*A[0] > combi[-1]*A[-1]:
                    del combi[-1]
                    combi.insert(0,A[0])
                else:
                    del combi[0]
                    combi.append(A[-1])
            elif A[-1] <= 0:
                del combi[-1]
                combi.insert(0,A[0])

    answer =  functools.reduce(multiply,combi)
print(answer)
