while True:
    h=[]
    S=input()
    if S=="-":
        break
    m=int(input())
    for i in range(m):
        h=int(input())
        if len(S)==h:
            pass
        else:
            S=S[h:]+S[:h]
    print(S)