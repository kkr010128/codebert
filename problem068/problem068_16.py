S = str(input())
for i in range(int(input())):
    L = input().split()
    o = L[0]
    a = int(L[1])
    b = int(L[2]) + 1
    if len(L) == 4:
        p = L[3]
    else:
        p = 0

    if o == "print":
        print(S[a:b])
    elif o == "reverse":
        S = S[:a]+S[a:b][::-1]+S[b:]
    elif o == "replace":
        S = S[:a]+p+S[b:]

