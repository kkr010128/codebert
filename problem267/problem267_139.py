def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(1000):
        d0 = str(i % 10)
        d1 = str((i // 10) % 10)
        d2 = str((i // 100) % 10)
        j = 0
        found = False
        while j < N:
            if S[j] == d0:
                found = True
                j += 1
                break
            j += 1
        if not found:
            continue
        found = False
        while j < N:
            if S[j] == d1:
                found = True
                j += 1
                break
            j += 1
        if not found:
            continue
        found = False
        while j < N:
            if S[j] == d2:
                found = True
                j += 1
                break
            j += 1
        if not found:
            continue
        if found:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
