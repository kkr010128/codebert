import sys
input = sys.stdin.readline
import math
a = math.sqrt(3) * 0.5
def koch(d, p1, p2):
    if d == 0:
        return
    else:
        s = [(2*p1[0]+p2[0])/3, (2*p1[1]+p2[1])/3]
        t = [(p1[0]+2*p2[0])/3, (p1[1]+2*p2[1])/3]
        u = [(t[0]-s[0])*0.5-(t[1]-s[1])*a+s[0], (t[0]-s[0])*a+(t[1]-s[1])*0.5+s[1]]
        koch(d-1, p1, s)
        print(s[0], s[1])
        koch(d-1, s, u)
        print(u[0], u[1])
        koch(d-1, u, t)
        print(t[0], t[1])
        koch(d-1, t, p2)

def main():
    n = int(input())
    p1 = [0, 0]
    p2 = [100, 0]
    print(p1[0], p1[1])
    koch(n, p1, p2)
    print(p2[0], p2[1])


if __name__ == '__main__': main()
