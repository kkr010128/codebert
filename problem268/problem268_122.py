import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7

def main():
    N,*A = map(int, read().split())

    cnt = [0] * N
    ans = 1
    for a in A:
        if a == 0:
            cnt[0] += 1
            continue
        ans *= cnt[a - 1] - cnt[a]
        ans %= MOD
        cnt[a] += 1
        
    if cnt[0] == 1:
        ans *= 3
    elif cnt[0] <= 3:
        ans *= 6
    else:
        ans = 0
    
    ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
