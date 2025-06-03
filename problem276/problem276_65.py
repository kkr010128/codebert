from sys import stdin
import itertools
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    a=list(map(int,readline().split()))

    s1=[0]*n
    s2=[0]*n
    for i in range(n):
        if i==0:
            s1[i]=a[i]
        else:
            s1[i]+=s1[i-1]+a[i]

    for i in range(n-1,-1,-1):
        if i==n-1:
            s2[i]=a[i]
        else:
            s2[i]+=s2[i+1]+a[i]

    ans=float("inf")
    for i in range(n-1):
        ans=min(ans,abs(s1[i]-s2[i+1]))

    print(ans)

if __name__=="__main__":
    main()