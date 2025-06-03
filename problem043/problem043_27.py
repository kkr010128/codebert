class SwappingTwoNumbers:
    def output(self, n):
        n.sort()
        print "%d %d" % (n[0], n[1])

if __name__ == "__main__":
    stn = SwappingTwoNumbers();
    while True:
        n = map(int, raw_input().split())
        if n[0] == 0 and n[1] == 0:
            break
        stn.output(n)