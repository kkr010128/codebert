import sys
num = 0

while 1:
    x = sys.stdin.readline().strip()
    if x == "0":
        break
    num = num + 1
    print("Case " + str(num) + ": " + x)