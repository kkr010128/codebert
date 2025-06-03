import math
def calc_combi(n,m):
    if n<=1:
        return 0
    return math.factorial(n)/(math.factorial(m)*(math.factorial(n-m)))
n,m=map(int,input().split())
ans=int(calc_combi(n,2)+calc_combi(m,2))
print(ans)