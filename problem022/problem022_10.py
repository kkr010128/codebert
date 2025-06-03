def main():
    n = int(input())
    S = list(map(int,input().split()))
    q = int(input())
    T = list(map(int,input().split()))

    cnt = 0
    S.sort()
    for i in range(n):
        if i == 0:
            if S[i] in T:
                cnt += 1
                continue
        if (S[i] in T) and (S[i] != S[i-1]):
            cnt += 1

    return cnt

print(main())

