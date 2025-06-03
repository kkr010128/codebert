
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def main():
    l, r = tuple(map(int, input().split(' ')))
    print(gcd(l, r))

main()
