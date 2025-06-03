import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n, m = MI()
    ac = [False]*(n+1)
    wa = [0]*(n+1)
    for _ in range(m):
        temp = input().split()
        p, s = int(temp[0]), temp[1]
        if not ac[p]:
            if s == 'AC':
                ac[p] = True
            else:
                wa[p] += 1
    penalty = 0
    for i in range(n+1):
        if ac[i]:
            penalty += wa[i]
    print('{} {}'.format(sum(ac), penalty))

if __name__ == '__main__':
    main()