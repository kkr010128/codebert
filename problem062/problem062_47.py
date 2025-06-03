from sys import stdin

while True:
    x = [int(i) for i in list(stdin.readline().rstrip())]
    if len(x) == 1 and x[0] == 0:
        break
    else:
        print(sum(x))
