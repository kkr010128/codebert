class ReversingNumbers:
    def output(self, a):
        s = ""
        a.reverse()
        for i in range(len(a)-1):
            s += "%d " % (a[i])
        s += "%d" % (a[len(a)-1])
        print s

if __name__ == "__main__":
    rn = ReversingNumbers()
    raw_input()
    a = map(int, raw_input().split())
    rn.output(a)