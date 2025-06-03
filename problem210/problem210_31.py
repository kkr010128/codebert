#https://tjkendev.github.io/procon-library/python/range_query/rmq_segment_tree.html
# N: 処理する区間の長さ

#bit管理
#演算はor
N = int(input())
s = input()


N0 = 1
while N0<=N:
    N0*=2
INF = 0
data = [0]*(2*N0)
# a_k の値を x に更新
def update(k, x):
    k += N0-1
    data[k] = 1<<x
    while k >= 0:
        k = (k - 1) // 2
        data[k] =data[2*k+1]|data[2*k+2]
# 区間[l, r)の最小値
def query(l, r):
    L = l + N0; R = r + N0
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = s|data[R-1]

        if L & 1:
            s = s|data[L-1]
            L += 1
        L >>= 1; R >>= 1
    return s

for i in range(N):
    update(i,ord(s[i])-ord("a"))
q = int(input())

for j in range(q):
    t,l,r = input().split( )
    if t=="1":
        update(int(l)-1,ord(r)-ord("a"))
        
    else:
        bit = bin(query(int(l)-1,int(r)))[2:]
        ans = 0
        for i in bit:
            ans += int(i)
        print(ans)