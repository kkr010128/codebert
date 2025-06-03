S = list(input())
q = int(input())
for i in range(q):
    cmd, a, b, *c = input().split()
    a = int(a)
    b = int(b)
    if cmd == "replace":
        S[a:b+1] = c[0]
    elif cmd == "reverse":
        S[a:b+1] = reversed(S[a:b+1])
    else:
        print(*S[a:b+1], sep='')

