import sys

def main():
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))

    s = input()
    p = input()
    cnt = 0
    for i in range(len(s) - len(p)+1):
        mx = 0
        for j in range(len(p)):
            if s[i+j] == p[j]:
                mx += 1
            # print(i, mx)
        cnt = max(cnt, mx)

    # print(p,cnt)
    print(len(p)-cnt)

if __name__ == '__main__':
    main()
