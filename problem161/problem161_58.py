def inN():
    return int(input())
def inL():
    return list(map(int,input().split()))
def inNL(n):
    return [list(map(int,input().split())) for i in range(n)]

a,b,n = inL()

x = min(b-1,n)
print(int(a*x/b)-a*int(x/b))
