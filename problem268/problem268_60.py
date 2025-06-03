MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)



def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = [0] * (n + 1)
    cnt[0] = 3
    
    ans = 1
    for num in a:
        ans *= cnt[num]
        ans %= MOD
        cnt[num] -= 1
        cnt[num + 1] += 1
    
    print(ans)

if __name__ =='__main__':
    main()   
