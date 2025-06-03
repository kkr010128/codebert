import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

a, b = inintm()

for i in range(10001):
    if i*0.08//1 == a and i*0.1//1 == b:
        print(i)
        exit()

print(-1)
