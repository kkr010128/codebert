import sys
input = sys.stdin.buffer.readline
from collections import defaultdict

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    
    d = defaultdict(int)
    cum = [0]
    for i in range(N):
        cum.append((cum[-1]+a[i]-1)%K)
    
    ans = 0
    for i in range(N+1):
        ans += d[cum[i]]
        d[cum[i]] += 1
        if i >= K-1:
            d[cum[i-K+1]] -= 1
    
    print(ans)
    
if __name__ == "__main__":
    main()
