def set1():
    N,M = [int(i) for i in input().split()]
    H = [int(i) for i in input().split()]
    set_N = set([i for i in range(1, N+1)])
    for i in range(M):
        A,B = [int(i) for i in input().split()]
        if H[A-1] < H[B-1]:
            if A in set_N:
                set_N.remove(A)
        elif H[B-1] < H[A-1]:
            if B in set_N:
                set_N.remove(B)
        else:
            if A in set_N:
                set_N.remove(A)
            if B in set_N:
                set_N.remove(B)
    print(len(set_N))

if __name__ == "__main__":
    set1()