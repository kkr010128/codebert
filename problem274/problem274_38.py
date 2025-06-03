import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = list(map(int, input().split()))
s = input()
c = n
ans = []
while c>0:
    val = None
    for i in range(1,m+1):
        if c-i>=0 and s[c-i]=="0":
            val = i
    if val is None:
        ans = -1
        break
    c = c-val
    ans.append(val)
if ans==-1:
    print(ans)
else:
    write(" ".join(map(str, ans[::-1])))