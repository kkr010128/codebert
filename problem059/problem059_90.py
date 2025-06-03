# AOJ ITP1_7_C

def numinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    a = numinput()
    r = a[0]; c = a[1]
    M = []
    for i in range(r):
        M.append(numinput())  # あ、そうか。。
        sum = 0
        for j in range(c): sum += M[i][j]
        M[i].append(sum)
    list = []
    for j in range(c + 1):
        sum = 0
        for i in range(r): sum += M[i][j]
        list.append(sum)
    M.append(list)

    for i in range(r + 1):
        _str_ = ""
        for j in range(c):
            _str_ += str(M[i][j]) + " "
        _str_ += str(M[i][c])
        print(_str_)

if __name__ == "__main__":
    main()
