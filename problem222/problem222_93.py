from collections import defaultdict
def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    d = defaultdict(lambda:0)
    for i in range(n):
        d[a[i]] += 1
    if max(d.values()) >1:
        print("NO")
    else:
        print("YES")
        
if __name__ == "__main__":
    main()