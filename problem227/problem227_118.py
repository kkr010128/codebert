import sys

def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    N, K = MI()
    H = LI()
    Hs = sorted(H)
    ans = 0

    if N > K:
        for i in range(N-K):
            ans += Hs[i]
        print(ans)
    else:
        print(0)

if __name__ == "__main__":
	main()