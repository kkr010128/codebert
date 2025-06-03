while True:
    C=input()
    if C=="-":
        break
    else:
        m=int(input())
        for i in range(m):
            h=int(input())
            c=C[0 : h]
            C=C[h : len(C) + 1]
            C+=c
        print(C)
