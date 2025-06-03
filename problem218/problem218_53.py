from collections import Counter
def main():
    n = int(input())
    S = [input() for _ in range(n)]
    c = Counter(S).most_common()
    V = c[0][1]
    ans = [k for k, v in c if v == V]
    [print(a) for a in sorted(ans)]

if __name__ == '__main__':
    main()
