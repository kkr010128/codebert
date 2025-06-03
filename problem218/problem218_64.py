from collections import Counter


def main():
    n = int(input())
    s = (input() for i in range(n))
    d = Counter(s)
    num = d.most_common(1)[0][1]
    ans = sorted(j[0] for j in d.items() if j[1] == num)
    for i in ans:
        print(i)

main()