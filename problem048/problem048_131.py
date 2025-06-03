class MinMaxAndSum:
    def output(self, a):
        print "%d %d %d" % (min(a), max(a), sum(a))

if __name__ == "__main__":
    mms = MinMaxAndSum()
    raw_input()
    a = map(int, raw_input().split())
    mms.output(a)