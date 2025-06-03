# coding: utf-8
def main():
    n, m, l = map(int, raw_input().split())
    mat_A = [] # (n, m)
    mat_B = [] # (m, l)
    for i in range(n):
        mat_A.append(map(int, raw_input().split()))

    for j in range(m):
        mat_B.append(map(int, raw_input().split()))

    for i in range(n):
        c = [0 for g in range(l)]
        for j in range(l):
            for k in range(m):
              #  print "n:{}, m:{}, l:{}".format(i,k,j)
                try:
                    c[j] += mat_A[i][k] * mat_B[k][j]
                except:
                    print "n: {}, m: {}, l: {}".format(i,k,j)
        print " ".join(map(str, c))
if __name__ == "__main__":
    main()