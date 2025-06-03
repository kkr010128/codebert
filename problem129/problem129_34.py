import sys
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve():
    m = a[-1]+1
    ava = [0]*m
    for rep in a:
        ava[rep] += 1
        if ava[rep]==1:
            for item in range(2*rep,m,rep):
                ava[item] += 2

    print(ava.count(1))
    return

if __name__=='__main__':
    n = I()
    a = list(IL())
    a.sort()
    solve()