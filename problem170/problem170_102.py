import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    nums = [i for i in range(n+1)]
    sums = [0]
    ans = 0
    x = 10**9 + 7
    for i in range(n):
        sums.append(nums[i+1]+sums[i])
    for j in range(k, len(nums)+1):
        if j == len(nums):
            ans += 1
        else:
            ans += sums[-1] - sums[-(1+j)] - sums[j-1] + 1
    print(ans%x)   

if __name__ == '__main__':
    main()