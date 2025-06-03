def main():
    t1, t2 = map(int, raw_input().split())
    a1, a2 = map(int, raw_input().split())
    b1, b2 = map(int, raw_input().split())
    ax1 = t1 * a1
    bx1 = t1 * b1
    ax2 = t2 * a2
    bx2 = t2 * b2
    if ax1 + ax2 == bx1 + bx2:
        print 'infinity'
        return
    if ax1 + ax2 < bx1 + bx2:
        ax1, bx1 = bx1, ax1
        ax2, bx2 = bx2, ax2
    init_d = bx1 - ax1
    if init_d < 0:
        print 0
        return
    total_delta = ax1 + ax2 - bx1 - bx2
    ans = 1 + (init_d / total_delta) * 2
    if init_d % total_delta == 0:
        ans -= 1
    print ans

main()
