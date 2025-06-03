N, A, B = [int(a) for a in input().split()]

ans = 0
repseq = N // (A + B)
ans = repseq * A

lastseq = N%(A+B)

if A >= lastseq:
    ans += lastseq
else:
    ans += A

print(ans)