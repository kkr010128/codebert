from collections import Counter
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

    a = [0]
    s = 0
    for i in range(N):
        s += S[i] * pow(10, i, P)
        a.append(s % P)
    
    t = Counter(a)

    ans = 0
    for v in t.values():
        ans += v * (v-1) // 2
    
    print(ans)

    


if __name__ == "__main__":
    main()
