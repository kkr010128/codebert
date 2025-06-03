def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))

    left = 0
    right = max(A)

    while abs(right-left)>1:
        cent = (right+left)//2
        
        ct = 0
        for a in A:
            ct+=(a-0.1)//cent
        
        if ct <= k:
            right=cent
        else:
            left=cent
    
    print(right)
main()