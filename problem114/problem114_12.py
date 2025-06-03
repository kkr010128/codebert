import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    D = int(input())
    c = [0] + list(map(int, input().split()))
    s = [[0]*27]
    t = [0]
    satisfy = 0
    last = [0] * 27
    for _ in range(D):
        s.append([0] + list(map(int, input().split())))
    for _ in range(D):
        t += [int(input())]
    for i in range(1, D+1):
        decrease = 0
        last[t[i]] = i
        for j in range(1, 27):
            decrease += (c[j] * (i - last[j]))
        satisfy += (s[i][t[i]] - decrease)
        print(satisfy)

if __name__ == '__main__':
    main()