'''
0から9までの数字から成る長さNの文字列Sの部分文字列の内、
十進数表記の整数とみなした時、素数Pで割り切れるものの個数を求めよ。
部分文字列は先頭が0であっても良く、文字列の位置で区別する。

terms:
    1<=n<=2*10**5
    2<=p<=10**4

input:
    4 3
    3543

output:
    6
'''

from collections import defaultdict
import sys
input = sys.stdin.readline
INF = float('inf')
mod = 10 ** 9 + 7
eps = 10 ** -7
def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))
n, p = inpl()
s = input()[:-1]
arr = [int(s[i]) for i in range(n)]
ans = 0
if p == 2 or p == 5:
    '''
    10を割り切ると桁の話が使えないので場合分け
    1の位が割り切れればそれだけ
    '''
    for i in range(n):
        if arr[i] % p == 0:
            ans += i + 1
    print(ans)
else:
    '''
    Pが10の約数である2,5だと以下の仮定が成り立たないので使えない
    ・ある数XがPで割り切れるならそれを10倍したものもPで割り切れる

    f(i)=Sの下i桁をPで割った時の余り
    として、f(i)=f(j)になる組を考える。
    するとiからj桁目までの値はPで割り切れる(i%p-j%p≡(i-j)%p)
    pow(x,y,z)=x^y%z
    '''
    dic = defaultdict(int)
    # dic = { 余り: 個数}
    now = 0
    dic[0]=1 # 余り0ならまず条件一致。それ以外だったら同じあまりが出た時点で条件一致
    for i in range(n-1,-1,-1): #下i桁をpで割った余り
        now += arr[i] * pow(10, n - 1 - i, p)
        now %= p
        ans+=dic[now]
        dic[now] += 1
    
    print(ans)