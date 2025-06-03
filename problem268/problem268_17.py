def main():
    n=int(input())
    lst=list(map(int,input().split()))
    mod=10**9+7
    sm=1
    color=[0,0,0]
    for x in lst:
        if x not in color : sm=0;break
        sm*=color.count(x)
        sm%=mod
        color[color.index(x)]+=1
    print(sm)

main()