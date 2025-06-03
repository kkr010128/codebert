import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
s = input()
def snx(s, target=None, reverse=False, loop=False):
    """文字列sの各要素について、cがiより→で最初に現れる位置n[i][c]
    loop=Trueのとき周回した先のインデックスまで求める
    """
    if target is None:
        target = [chr(v) for v in range(ord("a"), ord("z")+1)]
    d = {c:None for c in target}
    nx = [[None]*len(target) for _ in range(len(s))]
    if not reverse:
        i = len(s)-1
        for c in reversed(s):
            d[c] = i
            for j,t in enumerate(target):
                nx[i][j] = d[t]
            i -= 1
        if loop:
            for i in range(len(s)):
                for j in range(len(target)):
                    if nx[i][j] is None:
                        nx[i][j] = nx[0][j]
    else:
        i = 0
        for c in s:
            d[c] = i
            for j,t in enumerate(target):
                nx[i][j] = d[t]
            i += 1
        if loop:
            for i in range(len(s)):
                for j in range(len(target)):
                    if nx[i][j] is None:
                        nx[i][j] = nx[-1][j]
    return nx
nx = snx(s, target=list(map(str, range(10))))
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            try:
                if nx[0][i] is not None and nx[nx[0][i]+1][j] is not None and nx[nx[nx[0][i]+1][j]+1][k] is not None:
#                     print(i, j, k)
                    ans += 1
            except IndexError:
                pass
print(ans)