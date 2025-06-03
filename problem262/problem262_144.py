import itertools

def main():
    N = int(input())
    BIT = list(itertools.product([True,False], repeat=N))
    P = [[(0,0)]]
    for i in range(1,N+1):
        A =  int(input())
        L = []
        for _ in range(A):
            x,y = map(int,input().split())
            L.append((x,y))
        P.append(L)

    ans = 0

    for b in BIT:
        cnt = 0
        flag = True
        HU = [-1]*(N+1)
        for i in range(1,N+1):
            if b[i-1]:
                cnt += 1
                for hu in P[i]:
                    if b[hu[0]-1] != (hu[1]==1):
                        flag = False
                        break
        if flag:
            ans = max(ans,cnt) 


    print(ans)


if __name__ == '__main__':
    main()