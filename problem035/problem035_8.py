class XCubic:
    def exe(self, x):
        return x*x*x

if __name__ == "__main__":

    x = int(raw_input())
    xc = XCubic()
    print(xc.exe(x))