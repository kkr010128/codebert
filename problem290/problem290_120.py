

def resolve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    F= list(map(int,input().split()))

    A.sort()
    F.sort(reverse = True)
    AF  = list(zip(A,F))

    if sum(A)<=K:
        print(0)
        return
    l = 0
    r = max([i*j for i,j in AF])
    center =0
    while l < r-1:

        center = (l+r)//2
        score =sum([max(0,a-center//f) for a,f in AF])
        
        if score > K:
            l = center
        else:
            r = center

    print(r)





if __name__ == "__main__":
    resolve()