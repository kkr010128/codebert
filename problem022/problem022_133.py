def run():
    s_n = int(input())
    S = set(map(int, input().split()))
    t_n = int(input())
    T = set(map(int, input().split()))

    print(len(S&T))

if __name__ == '__main__':
    run()


