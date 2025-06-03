import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N, P = map(int, readline().split())
    S = [int(i) for i in readline().strip()[::-1]]

    ans = 0
    if P == 2 or P == 5:
        for i, s in enumerate(S):
            if s % P == 0:
                ans += N - i
        print(ans)
        exit()

    a = {}
    a[0] = 1
    t = 0
    x = 1
    for s in S:
        t += s * x
        t %= P
        
        if t in a:
            a[t] += 1
        else:
            a[t] = 1

        x *= 10
        x %= P
    
    ans = 0
    for v in a.values():
        ans += v * (v-1) // 2
    
    print(ans)
    

if __name__ == "__main__":
    main()
