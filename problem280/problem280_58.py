import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    lst = [None, ]
    for _ in range(n):
        x, y = LI()
        lst.append((x,y))

    per = itertools.permutations(range(1,n+1))
    sm = 0
    oc = math.factorial(n)
    for p in per:
        dist = 0
        before = p[0]
        for place in p[1:]:
            dist += math.sqrt((lst[place][0]-lst[before][0])**2 + (lst[place][1]-lst[before][1])**2)
            before = place
        sm += dist
    ans = sm/oc
    print(ans)
main()
