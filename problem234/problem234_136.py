from collections import defaultdict

def main():
    n = int(input())
    d = defaultdict(int)
    for i in range(1, n+1):
        s = str(i)
        a = s[0]
        b = s[-1]
        d[a, b] += 1
    ans = 0
    d_items = list(d.items())
    for (a, b), v in d_items:
        ans += v * d[b,a]
    print(ans)
    
if __name__ == '__main__':
    main()