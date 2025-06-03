import math
N,M=map(int,input().split())

def comb(num,k):
    if num<2:
        return 0
    return math.factorial(num)/(math.factorial(k)*math.factorial(num-k))

ans=int(comb(N,2)+comb(M,2))

print(ans)