def main():
    n = int(input())
    L = []
    for _ in range(n):
        x,l = map(int,input().split())
        L.append([x+l,x-l])

    L.sort()

    cnt = 0
    right = -10**9
    for r,l in L:
        if right <= l:
            cnt += 1
            right = r

    print(cnt)

main()