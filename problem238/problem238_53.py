#%% for atcoder uniittest use
import sys
input= lambda: sys.stdin.readline().rstrip()
def pin(type=int):
    return map(type,input().split())

#%%code

def resolve():
    bigint=10**9
    N,K,S=pin()
    if S!=bigint:
        print(*([bigint]*(N-K)+[S]*(K)))
        return
    print(*([1]*(N-K)+[bigint]*K))
    
    
#%%submit!
resolve()