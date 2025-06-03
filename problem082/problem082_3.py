from sys import stdin
def ip(): return [int(i) for i in stdin.readline().split()]
def sp(): return [str(i) for i in stdin.readline().split()]


s = str(input())
t = str(input())

ans = len(t)
for i in range(len(s) - len(t) + 1):
    # print(f'{i=} | {ans=}')
    curr = len(t)
    for j in range(i, len(t) + i):
        # print(f'{curr=} | {s[j]=} | {t[j-i]=}')
        if s[j] == t[j-i]:
            curr -= 1
    ans = min(ans, curr)
print(ans)
