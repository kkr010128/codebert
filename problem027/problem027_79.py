from math import sqrt

def koch(n, c1, c2):
    if n == 0:
        return
    
    # 処理
    v = [c2[0] - c1[0], c2[1] - c1[1]]

    s = [c1[0] + v[0] / 3, c1[1] + v[1] / 3]
    t = [c1[0] + 2 * v[0] / 3, c1[1] + 2 * v[1] / 3]
    u = [c1[0] + v[0]/2 - v[1] * sqrt(3) / 6, c1[1] + v[1]/2 + v[0] * sqrt(3) / 6]

    koch(n-1, c1, s)
    print(" ".join(map(str, s)))
    koch(n-1, s, u)
    print(" ".join(map(str, u)))
    koch(n-1, u, t)
    print(" ".join(map(str, t)))
    koch(n-1, t, c2)


    

def main():
    fmt = "%.8f %.8f"
    q3 = sqrt(3)

    c1 = [0, 0]
    c2 = [100, 0]

    n = int(input())
    print(fmt % tuple(c1))
    koch(n, c1, c2)
    print(fmt % tuple(c2))

main()
