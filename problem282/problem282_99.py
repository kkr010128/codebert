import sys
input = sys.stdin.buffer.readline
from operator import itemgetter
import numpy as np

def main():
    N,T = map(int,input().split())
    food = []
    for _ in range(N):
        a,b = map(int,input().split())
        food.append((a,b))
        
    dp = np.zeros(T,dtype=int)
    food.sort(key = itemgetter(0))
    
    ans = 0
    for a,b in food:
        ans = max(ans,dp[-1]+b)
        dp[a:] = np.maximum(dp[a:],dp[:-a]+b)

    print(ans)
    
if __name__ == "__main__":
    main()