import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().strip()

def main():
    S = input()
    print("Yes" if S[2]==S[3] and S[4]==S[5] else "No")

main()
