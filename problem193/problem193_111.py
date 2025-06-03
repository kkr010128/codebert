import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    H,W,K = map(int, readline().split())
    S = [readline().strip() for j in range(H)]

    white = []
    for line in S:
        white.append(line.count("1"))
    white_total = sum(white)

    if white_total <= K:
        print(0)
        exit()

    ans = 10**5
    for i in range(2**(H-1)):
        impossible = False
        x = 0
        ly = bin(i).count("1")
        y_sum = [0]*(ly + 1)
        j = 0
        while j < W:
            m = 0
            y = [0]*(ly + 1)
            for k in range(H):
                if S[k][j] == "1":
                    y[m] += 1
                    if y[m] > K:
                        impossible = True
                        break
                    y_sum[m] += 1
                    if y_sum[m] > K:
                        x += 1
                        y_sum = [0]*(ly + 1)
                        j -= 1
                        break
                if (i >> k) & 1:
                    m += 1
            j += 1
            if impossible:
                x = 10**6
                break

        ans = min(ans, x + ly)

    print(ans)


if __name__ == "__main__":
    main()
