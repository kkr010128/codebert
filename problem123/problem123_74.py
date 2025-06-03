def resolve():
    n = int(input())
    a = list(map(int, input().split()))

    all_xor = 0
    for ai in a:
        all_xor ^= ai

    ans = []

    for ai in a:
        ans.append(str(all_xor ^ ai))

    print(' '.join(ans))

resolve()