import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for line in sys.stdin:
    line = line.strip()
    if line == "":
        break

    X = int(line)
    ans = 360 // gcd(X, 360)
    print(ans)