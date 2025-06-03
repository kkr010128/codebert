def resolve():
    N = int(input())
    X = input()
    Xint = int(X,2)
    popX = X.count("1")
    if popX == 1:
        idx = X.find("1")
        for i in range(N):
            if i == idx:
                print(0)
            else: 
                if i != N-1:
                    if X[-1] == "0":
                        print(1)
                    else:
                        print(2)
                else:
                    print(2)
        return

    Xmod_plus =  Xint % (popX+1)
    Xmod_minus = Xint % (popX-1)

    pop_2expi_p = {0:1}
    pop_2expi_m = {0:1}
    for i in range(1,N):
        pop_2expi_p[i] = pop_2expi_p[i-1] * 2 % (popX+1)
        pop_2expi_m[i] = pop_2expi_m[i-1] * 2 % (popX-1)

    for i in range(N):
        count = 1
        if X[i] == "1":
            nX = (Xmod_minus - pop_2expi_m[N-1-i] ) % (popX-1) 
        if X[i] == "0":
            nX = (Xmod_plus + pop_2expi_p[N-1-i] ) % (popX+1) 
        for j in range(N):
            if nX == 0:
                break
            else:
                nX %= bin(nX).count("1")              
                count += 1
        print(count)
resolve()