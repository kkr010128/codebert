import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    s = list(input())
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    cnt = r*g*b
    for i in range(n):
        for j in range(i+1, n):
            k = 2*j - i
            if k >= n:
                break
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                cnt -= 1
    print(cnt)

if __name__ == '__main__':
    main()