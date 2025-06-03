ii = lambda:int(input())
mi = lambda:list(map(int,input().split()))
ix = lambda x:list(input() for _ in range(x))
mix = lambda x:list(mi() for _ in range(x))
iix = lambda x:list(int(input()) for _ in range(x))
##########

def resolve():
    h1,m1,h2,m2,k = mi()
    res = convert(h2,m2) - convert(h1,m1) - k
    print(res)

def convert(h,m):
    return h*60 + m

if __name__ == "__main__":
    resolve()