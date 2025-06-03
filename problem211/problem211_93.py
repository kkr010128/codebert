
url = "https://atcoder.jp//contests/abc156/tasks/abc156_a"

def main():
    n, r = list(map(int, input().split()))
    print(r) if n >= 10 else print(r + 100 * (10 - n))

if __name__ == '__main__':
    main()
