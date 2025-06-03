import sys, math

h, w, n = [int(i) for i in sys.stdin.readlines()]

bigger = h if h >= w else w
print(math.ceil(n / bigger))