MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n,k,c = map(int,input().split())
    s = input()

    R = [-1] * k
    L = [-1] * k
    day = INF
    cnt = 0
    for i in range(n):
        if s[i] == 'o':
            if day > c:
                L[cnt] = i
                cnt += 1
                if cnt == k:
                    break
                day = 1
            else:
                day += 1
        else:
            day += 1
    
    day = INF
    cnt = k - 1
    for i in range(n - 1,-1,-1):
        if s[i] == 'o':
            if day > c:
                R[cnt] = i
                cnt -= 1
                if cnt < 0:
                    break
                day = 1
            else:
                day += 1
        else:
            day += 1
    
    ans = []
    for j in range(k):
        if R[j] == L[j]:
            ans.append(R[j] + 1)

    print(*ans,sep = '\n')

if __name__ =='__main__':
    main()  