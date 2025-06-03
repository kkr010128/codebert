def swap(x, y):
    tmp = x
    x = y
    y = tmp

def gcm(x, y):
    if x < y:
        swap(x, y)
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

if __name__ == '__main__':
    x, y = list(map(int, input().split()))
    n = gcm(x, y)
    print(n)