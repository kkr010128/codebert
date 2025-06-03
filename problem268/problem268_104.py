def f():
    n=int(input())
    l=[0,0,0]
    ans=1
    mod=10**9+7
    for i in list(map(int,input().split())):
        if i not in l:print(0);exit()
        ans=ans*l.count(i)%mod
        l[l.index(i)]+=1
    print(ans)
if __name__ == "__main__":f()