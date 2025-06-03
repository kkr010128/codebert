n,r=map(int,input().split())
def rate(n,r):
    if n>=10:
        return r
    else:
        return r+100*(10-n)

print(rate(n,r))