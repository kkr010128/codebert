class PrintAChessboard:
    def output(self, H, W):
        s1 = ""
        s2 = ""
        for w in range(W):
            if w % 2 == 0:
                s1 += "#"
                s2 += "."
            else:
                s1 += "."
                s2 += "#"
        for h in range(H):
            if h % 2 == 0:
                print s1
            else:
                print s2
        print

if __name__ == "__main__":
    pc = PrintAChessboard()
    while True:
        h, w = map(int, raw_input().split())
        if h == 0 and w == 0:
            break
        pc.output(h, w)