import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    S = sys.stdin.readline().rstrip()

    cnt = 0
    for i in range(10):
        pos_1 = S.find(str(i))
        if pos_1 == -1 or pos_1 > N - 3:
            continue

        for j in range(10):
            pos_2 = S[pos_1 + 1:].find(str(j))
            if pos_2 == -1 or pos_2 > N - 2:
                continue

            for k in range(10):
                pos_3 = S[pos_1 + 1 + pos_2 + 1:].find(str(k))
                if pos_3 != -1:
                    cnt += 1

    print(cnt)


main()
