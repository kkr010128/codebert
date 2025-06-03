import sys
sys.setrecursionlimit(10**6)
def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    dp = [[10**5] * w for _ in range(h)]
    def func(temp, now, flag):
        x, y = now
        if y > h - 1 or x > w - 1:
            return 10**6
        if s[y][x] == "#":
            if not flag:
                temp += 1
            flag = True
        else:
            flag = False
        if x == w-1 and y == h-1:
            return temp
        if dp[y][x] <= temp:
            return 10**6
        dp[y][x] = temp
        piyo = []
        return min(func(temp, (x + 1, y), flag), func(temp, (x, y + 1), flag))
    print(func(0, (0, 0), False))
main()