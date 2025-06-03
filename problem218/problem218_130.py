from collections import defaultdict

def main():
    N = int(input())

    dd = defaultdict(int)

    for _ in range(N):
        si = input()
        dd[si] += 1

    maxv = max(dd.items(), key = lambda item: item[1])[-1]
    strings = [key for key, val in dd.items() if val == maxv]

    strings = sorted(strings)

    for string in strings:
        print(string)

if __name__ == '__main__':
    main()
