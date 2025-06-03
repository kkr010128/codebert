import math as mt

def kock(n, p1, p2):
    if n == 0:
        return
    s =[(2 * p1[0] + p2[0]) / 3 , (2 * p1[1] + p2[1]) / 3]
    t = [(p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3]
    u = [(t[0]-s[0])*mt.cos(mt.radians(60))
        -(t[1]-s[1])*mt.sin(mt.radians(60)) + s[0],
         (t[0]-s[0])*mt.sin(mt.radians(60))
         +(t[1]-s[1])*mt.cos(mt.radians(60)) + s[1]]

    kock(n-1, p1, s)
    print("{0:.8f} {1:.8f}".format(s[0],s[1]))
    kock(n-1, s, u)
    print("{0:.8f} {1:.8f}".format(u[0],u[1]))
    kock(n-1, u, t)
    print("{0:.8f} {1:.8f}".format(t[0],t[1]))
    kock(n-1, t, p2)


if __name__ == '__main__':
    n = int(input())
    p1 = (0,0)
    p2 = (100,0)
    print("{0:.8f} {1:.8f}".format(p1[0],p1[1]))
    kock(n, p1, p2)
    print("{0:.8f} {1:.8f}".format(p2[0],p2[1]))