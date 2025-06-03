# 最大公約数を求める
def gcm(m, n):
    # mを小さくする
    if m > n:
        _temp = n
        n = m
        m = _temp

    while m != 0:
        #print("{}, {}".format(m, n))
        m, n = n % m, m

    return n

a, b, = map(int, input().split())
g = gcm(a, b)

print("{}".format((int)(a * b / g)))