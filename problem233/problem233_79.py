import sys

def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]


def main():
    N = II()
    P = LI()
    ans = 0
    min = N+1

    for i in range(N):
        if P[i]<min:
            ans += 1
            min = P[i]

    print(ans)

if __name__ == "__main__":
	main()