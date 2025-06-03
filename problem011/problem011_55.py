import sys

def div(x, y):
    if x % y == 0:
        print y
    else:
        div(y, x%y)


line = sys.stdin.readline()
x, y = line.split(" ")

x = int(x)
y = int(y)

if x < y:
    x, y = y, x

if x == y:
    print x

else:
    div(x, y)