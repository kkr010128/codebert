class CircleInaRectangle:
    def __init__(self, W, H, x, y, r):
        if 0 <= x - r and 0 <= y - r and x + r <= W and y + r <= H:
            print "Yes"
        else:
            print "No"

if __name__ == "__main__":
    W, H, x, y, r = map(int, raw_input().split())
    CircleInaRectangle(W, H, x, y, r)