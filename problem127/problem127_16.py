from sys import stdin
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())


def main():
    X, Y = i_map()
    ans = False
    z = Y - (X * 2)
    if z < 0:
        pass
    elif z == 0 or (z % 2 == 0 and (z // 2) <= X):
        ans = True
    print("Yes" if ans else "No")

if __name__ == "__main__":
    main()
