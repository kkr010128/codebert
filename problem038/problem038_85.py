class SmallLargeOrEqual:
    def __init__(self, a, b):
        if a < b:
            print "a < b"
            return
        elif a > b:
            print "a > b"
            return
        else:
            print "a == b"
            return

if __name__ == "__main__":
    a,b = map(int,raw_input().split())
    SmallLargeOrEqual(a,b)