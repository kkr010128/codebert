# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()

def resolve():
    import sys
    input = sys.stdin.readline

    n = int(input().rstrip())

    s_list = [input().rstrip() for _ in range(n)]

    from collections import Counter
    c = Counter(s_list)

    max_count = c.most_common()[0][1]

    words = [word for word, count in c.most_common() if count == max_count]
    words.sort()
    print("\n".join(words))




if __name__ == "__main__":
    resolve()
