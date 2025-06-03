from collections import defaultdict
def main():
    n = int(input())
    s =defaultdict(lambda:0)
    for i in range(n):
        s[input()] += 1
    max_s = max(s.values())
    for key, value in sorted(s.items()):
        if value == max_s:
            print(key)

if __name__ == "__main__":
    main()