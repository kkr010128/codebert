def word():
    K = int(input())
    S = str(input())
    A = ""
    if len(S) <= K:
        print(S)
        return
    else:
        for i in range(K):
            A = A + S[i]
    A = A + "..."
    print(A)
    return
word()
