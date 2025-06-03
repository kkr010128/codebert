from sys import stdin
rs = stdin.readline
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    K = ri()
    A, B = ril()
    for i in range(A, B + 1):
        if i % K == 0:
            ans = 'OK'
            break
    else:
        ans = 'NG'
    print(ans)

if __name__ == '__main__':
    main()
