import math

class Circle:
    def output(self, r):
        print "%.6f %.6f" % (math.pi * r * r, 2.0 * math.pi * r)

if __name__ == "__main__":
    cir = Circle()
    r = float(raw_input())
    cir.output(r)