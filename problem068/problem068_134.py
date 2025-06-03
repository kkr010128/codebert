def main():
    m = list(input())
    q = int(input())
    A = []
    for _ in range(q):
        A.append(input().split())

    for x in range(q):
        if A[x][0] == "print":
            A[x][1] = int(A[x][1])
            A[x][2] = int(A[x][2])
            for y in range(A[x][1], A[x][2] + 1):
                if y != A[x][2]:
                    print(m[y], end = "")
                else:
                    print(m[y])
        elif A[x][0] == "reverse":
            A[x][1] = int(A[x][1])
            A[x][2] = int(A[x][2])
            hoge = []
            for y in range(A[x][1], A[x][2] + 1):
                hoge.append(m[y])
            hoge = hoge[::-1]
            i = 0
            for y in range(A[x][1], A[x][2] + 1): 
                m[y] = hoge[i]
                i += 1
        elif A[x][0] == "replace":
            A[x][1] = int(A[x][1])
            A[x][2] = int(A[x][2])
            fuga = list(A[x][3])
            j = 0
            for y in range(A[x][1], A[x][2] + 1):
                m[y] = fuga[j]
                j += 1


if __name__ == "__main__":
    main()