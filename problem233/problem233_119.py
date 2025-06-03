def main():
    n = int(input())
    P = [int(x) for x in input().split()]
    minv = 2 * 10 ** 5 + 1
    cnt = 0
    for i in range(n):
        if minv > P[i]:
            minv = P[i]
            cnt += 1
    print(cnt)
    
if __name__ == '__main__':
    main()