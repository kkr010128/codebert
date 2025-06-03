import sys

line = sys.stdin.readline()

tate, yoko = line.split(" ")

tate = int(tate)
yoko = int(yoko)

S = tate * yoko
T = 2 * (tate + yoko)

print '%d %d' % (S, T)