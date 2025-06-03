import sys

def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]

def main():
    C = str(input())

    n = ord(C) - ord('A') + 1

    ans = chr(n+64+1)

    print(ans)

if __name__ == "__main__":
	main()