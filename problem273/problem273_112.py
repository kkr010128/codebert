from collections import defaultdict 
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = 0
    ruiseki = [0]
    d = defaultdict(int)
    d[0]=1
    for i in range(n):
        if i - k + 1>= 0:
            d[ruiseki[i - k+1]]-=1
        ruiseki.append((ruiseki[i] + a[i] - 1)%k)
        ans += d[ruiseki[i+1]]
        d[ruiseki[i + 1]] += 1
    print(ans)
 
 
if __name__ == '__main__':
    main()