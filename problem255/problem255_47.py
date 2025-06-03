#https://atcoder.jp/contests/abc148/tasks/abc148_b
N = int(input())
a,b = map(str,input().split())
moji = ""
for i in range(N):
    moji += a[i]+b[i]

print(moji)