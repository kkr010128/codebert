def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    Min = [10**9]
    ans = 0
    for i in range(n):
        Min.append(min(Min[-1],p[i]))
    for i in range(n):
        if Min[i]>p[i]:
            ans += 1
    print(ans)
main()