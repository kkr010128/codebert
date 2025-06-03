import sys
def input(): return sys.stdin.readline().rstrip()
 
def main():
    n=int(input())
    A=list(map(int, input().split()))
    ans = 0
    mod = 10**9 + 7
    for i in range(60):
        q = sum(map(lambda x:((x >> i) & 0b1),A))
        ans += q*(n-q)*pow(2, i, mod)
        ans = ans % mod
    print(ans)
 
if __name__=='__main__':
    main()