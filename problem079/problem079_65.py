import sys
def input(): return sys.stdin.readline().rstrip()
 
 
def per(n, r, mod=10**9+7):  # 順列数
    per = 1
    for i in range(r):
        per = per*(n-i) % mod
    return per


def com(n, r, mod=10**9+7):  # 組み合わせ数
    r = min(n-r, r)
    bunshi = per(n, r, mod)
    bunbo = 1
    for i in range(1, r+1):
        bunbo = bunbo*i % mod
    return bunshi*pow(bunbo, -1, mod) % mod

def comH(n, r, mod=10**9+7): # n種類からr個取る重複組み合わせ数
    return com(n+r-1,r,mod)
 
def main():
    s = int(input())
    ans = 0
    for i in range(1, (s//3)+1):
        k = s-3*i
        ans += comH(i,k)
        #print(com(k+i,k),k+i,i)
    print(ans % (10**9+7))
 
 
if __name__ == '__main__':
    main()