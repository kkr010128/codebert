import sys
import collections
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = collections.Counter(a)
    all_comb = 0
    for i in cnt.keys():
        all_comb += cnt[i] * (cnt[i]-1) // 2
    for i in range(n):
        comb = all_comb
        comb -= cnt[a[i]] * (cnt[a[i]]-1) // 2
        comb += (cnt[a[i]]-1) * (cnt[a[i]]-2) // 2
        print(comb)
        
if __name__ == '__main__':
    main()