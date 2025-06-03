def main():
    N = int(input())
    A = list(map(int, input().split()))
    L = [0] * (10**6+1)
    for a in A:
        L[a] += 1
    ans = 0
    Ng = [False] * (10**6+1)
    for a, cnt in enumerate(L):
        if cnt:
            for i in range(a*2, 10**6+1, a):
                Ng[i] = True
    for a, (cnt, ng) in enumerate(zip(L, Ng)):
        if cnt == 1 and not ng:
            ans += 1
    print(ans)

main()
