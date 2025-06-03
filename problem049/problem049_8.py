class PrintARectangle:
    def output(self, H, W):
        s = ""
        for w in range(W):
            s += "#"
        for h in range(H):
            print s
        print

if __name__ == "__main__":
    pr = PrintARectangle()
    while True:
        h, w = map(int, raw_input().split())
        if h == 0 and w == 0:
            break
        pr.output(h, w)