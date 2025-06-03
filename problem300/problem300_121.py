import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b = list(map(int, input().split()))
def factor(n, m=None):
    # mを与えると、高々その素因数まで見て、残りは分解せずにそのまま出力する
    arr = {}
    temp = n
    M = int(-(-n**0.5//1))+1
    if m is not None:
        M = min(m+1, M)
    for i in range(2, M):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp] = 1

    if not arr:
        arr[n] = 1

    return arr
fa = factor(a)
fb = factor(b)
if 1 in fa:
    del fa[1]
if 1 in fb:
    del fb[1]
d = set(list(fa.keys())) & set(list(fb.keys()))
ans = len(d) + 1
print(ans)