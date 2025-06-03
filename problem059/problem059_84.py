def main():
    r, c = map(int, input().split())
    
    A = []
    for _ in range(r):
        A.append(list(map(int, input().split())))

    for x in range(r):
        hoge = 0
        for y in range(c):
            hoge += A[x][y]
        A[x].append(hoge)

    B = []
    for x in range(c):
        hoge = 0
        for y in range(r):
            hoge += A[y][x]
        B.append(hoge)

    total = 0
    for b in B:
        total += b
    
    B.append(total)
    A.append(B)

    for x in range(len(A)):
        for y in range(len(A[x])):
            if y != len(A[x]) - 1:
                print(A[x][y], end = " ")
            else:
                print(A[x][y])

if __name__ == "__main__":
    main()