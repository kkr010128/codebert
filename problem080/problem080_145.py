import sys
import itertools


def resolve(in_):
    N = int(next(in_))
    xy = (tuple(map(int, line.split())) for line in itertools.islice(in_, N))
    zw = tuple((x + y, x - y) for x, y in xy)

    zmax = zmin = zw[0][0]
    wmax = wmin = zw[0][1]
    for z, w in zw[1:]:
        zmax = max(zmax, z)
        zmin = min(zmin, z)
        wmax = max(wmax, w)
        wmin = min(wmin, w)

    ans = max(zmax - zmin, wmax - wmin)
    
    return ans
    

def main():
    answer = resolve(sys.stdin.buffer)
    print(answer)


if __name__ == '__main__':
    main()
