import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    N = int(input())
    word = []
    time = []
    for _ in range(N):
        a,b = input().split()
        word.append(a)
        time.append(int(b))
    X = input()
    s = -1
    for i in range(N):
        if word[i] == X:
            s = i + 1
    ans = sum(time[s:])
    print(ans)
if __name__ == '__main__':
    main()