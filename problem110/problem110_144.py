from sys import stdin

input = stdin.readline



def solve():
    Y, X, K = map(int, input().split())
    c = [inp for inp in stdin.read().splitlines()]
    res = 0
    for ymask in range((1<<Y) - 1):
        for xmask in range((1<<X) - 1):
            cnt = 0
            for y in range(Y):
                for x in range(X):
                    if ymask & (1<<y) == 0 and xmask & (1<<x) == 0 and c[y][x] == '#':
                        cnt += 1
            if cnt == K:
                res +=1
    print(res)



if __name__ == '__main__':
    solve()
