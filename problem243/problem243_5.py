import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    n=int(input())
    l=[list(input().split()) for i in range(n)]
    x=input()
    cnt=0
    for s,t in l:
        if s!=x:
            cnt+=int(t)
        elif s==x:
            cnt+=int(t)
            break
    suml=0
    for i in range(n):
        suml+=int(l[i][1])
    print(suml-cnt)

resolve()