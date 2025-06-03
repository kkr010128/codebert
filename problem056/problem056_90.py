import sys

def main():
    lines = sys.stdin.readlines()

    A = []
    B = []
    C = []
    n = 0
    m = 0
    for i, line in enumerate(lines):
        # print(line)
        # rm '\n' from string of a line
        line = line.strip('\n')
        elems = line.split(" ")
        if i == 0:
            n = int(elems[0])
            m = int(elems[1])
        elif 0 < i and i < n + 1:
            A.append([int(e) for e in elems])
        elif n < i:
            B.append([int(elems[0])])
    c = []
    for i in range(0, n):
        num = 0
        for index, e in enumerate(A[i]):
            num += e * B[index][0]
        c.append(num)

    for i in range(0, n):
        print c[i]

if __name__ == "__main__":
    main()