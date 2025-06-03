from collections import Counter
def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s_c = Counter(s)
    s_c_max = s_c.most_common()[0][1]
    keys =[k for k, v in s_c.items() if v == s_c_max]
    keys_s = sorted(keys)
    print(*keys_s, sep='\n')

if __name__ == '__main__':
    main()