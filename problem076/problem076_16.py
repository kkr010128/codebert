mod = 10**9 + 7
def C():
    N = int(input())
    ans = 10**N - 2*9**N + 8**N
    print(ans%mod)
def A():
    N = int(input())
    if( N == 0):
        print(1)
    else:
        print(0)
A()
