def main():
    n, m = map(int, input().split())
    p = (m+1)//2
    q = m//2
    l = 0
    r = 2*p-1
    for i in range(p):
        print(l+1, r+1)
        l += 1
        r -= 1
    l = 2*p
    r = l+2*q
    for i in range(q):
        print(l+1, r+1)
        l += 1
        r -= 1


main()
