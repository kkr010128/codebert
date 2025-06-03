import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    ls=len(s)
    a=[0]*(ls+1)
    for i in range(ls):
        if s[i]=='<':
            a[i+1]=a[i]+1
    for j in reversed(range(ls)):
        if s[j]=='>':
            a[j]=max(a[j+1]+1,a[j])
    print(sum(a))
resolve()