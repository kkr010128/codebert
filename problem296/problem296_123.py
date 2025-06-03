def main():
    S = input()
    K = int(input())
    A = []
    last = S[0]
    count = 1
    for i in range(1, len(S)):
        s = S[i]
        if last == s:
            count += 1
        else:
            A.append({'key': last, 'count': count})
            count = 1
        last = s
    A.append({'key': last, 'count': count})
    # print(A)
    if len(A) == 1:
        c = A[0]['count']
        l = c*K
        ans = l//2
        print(ans)
        return
    ans = 0
    if A[0]['key'] != A[-1]['key']:
        for a in A:
            c = a['count']
            ans += (c//2) * K
        print(ans)
        return
    for i in range(1, len(A) - 1):
        a = A[i]
        c = a['count']
        ans += (c//2) * K
    a0 = A[0]
    a1 = A[-1]
    c0 = a0['count']
    c1 = a1['count']
    ans += c0//2
    ans += c1//2
    ans += ((c0 + c1)//2) * (K - 1)
    print(ans)

if __name__ == '__main__':
    main()
