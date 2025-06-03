def main():
    import sys
    N = int(sys.stdin.readline())
    L = [0 for i in range(45)]
    L[0], L[1] = 1, 1
    for i in range(2, 45):
        L[i] = L[i-1] + L[i-2]
    #print(L)
    print(L[N])
    



if __name__=='__main__':
    main()
