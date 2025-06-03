import sys
input = sys.stdin.readline

def main():
    n, k = input_list()
    # R = グー, S = チョキ, P = パー
    R, S, P = input_list()
    t = input()
    tt = list(t)
    for i in range(n - k):
        if tt[i] == t[i+k]:
            tt[i+k] = "x"
    r = tt.count("r") * P
    s = tt.count("s") * R
    p = tt.count("p") * S
    print(r + s + p)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()
