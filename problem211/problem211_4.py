N, R = map(int, input().split())

if 10<=N:
    print(R)

elif N<10:
    x = R+(100*(10-N))
    print(x)
