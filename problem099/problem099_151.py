def main():
    import math
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    def f(a,l):
        ans = 0
        for i in range(len(a)):
            ans += math.ceil(a[i]/l)-1
        return ans
    l,r = 1,max(a)
    while r-l>1:
        mid = (l+r)//2
        g = f(a,mid)
        if g>k:
            l = mid+1
        else:
            r = mid
    if f(a,l)<=k:
        print(l)
    else:
        print(r)

if __name__ == "__main__":
    main()
