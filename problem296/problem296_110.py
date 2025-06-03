def main():
    S = input()
    k = int(input())
    if len(set(list(S))) == 1:
        print(len(S) * k // 2)
        exit()
    A = []
    cnt = 1
    tmp = S[0]
    for s in S[1::]:
        if s == tmp:
            cnt += 1
        else:
            A.append(cnt)
            tmp = s
            cnt = 1
    A.append(cnt)
    ans = sum([a // 2 for a in A])
    if S[0] == S[-1]:
        A[0] += A[-1]
        A.pop()
    ans += sum([a // 2 for a in A]) * (k - 1)
    print(ans)

if __name__ == '__main__':
    main()
