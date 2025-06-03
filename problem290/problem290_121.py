import sys
input = sys.stdin.buffer.readline

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    f = list(map(int,input().split()))
    
    a.sort()
    f.sort(reverse=True)
    
    l,r = -1,max(a)*max(f)+1
    
    while r-l>1:
        mid = (r+l)//2
        count = 0
        for cost,dif in zip(a,f):
            if mid >= cost*dif:
                continue
            rest = cost*dif-mid
            count += -(-rest//dif)
        if count <= K:
            r = mid
        else:
            l = mid
            
    print(r)

if __name__ == "__main__":
    main()
