def main():
    A,B,M=map(int,input().split())
    a=[int(_) for _ in input().split()]
    b=[int(_) for _ in input().split()]
    ans=min(a)+min(b)
    for m in range(M):
        x,y,c=map(int,input().split())
        ans=min(ans,a[x-1]+b[y-1]-c)
    print(ans)
main()